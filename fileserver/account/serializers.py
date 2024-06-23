from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from account.models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username','email','password','confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self,data):
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        if password == confirm_password:
            if len(password) < 6:
                raise serializers.ValidationError("Password must be at least 6 characters")
        else:
            raise serializers.ValidationError("Password does not match")
        return data
    
    def create(self,validated_data):
        validated_data.pop('confirm_password',None)
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email']

class CurrentUserPostSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ['id','username', 'email','post']