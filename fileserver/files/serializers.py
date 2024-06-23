from rest_framework import serializers
from files.models import Person,Color, Post
from django.contrib.auth import get_user_model


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
    def get_color_info(self,obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color name': color_obj.color_name,'hexcode': '#000555'}
    def validate(self,data):
        special_character = "!@#$%^&*()-_+?/<>"
        if data['age'] < 18:
            raise serializers.ValidationError("Age should be between 18 and 90")
        if any([i in special_character for i in data['name']]):
            raise serializers.ValidationError("Name should not contain special character")
        
        return data    
    
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at']
 