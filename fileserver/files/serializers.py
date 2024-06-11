from rest_framework import serializers
from files.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    def validate(self,data):
        special_character = "!@#$%^&*()-_+?/<>"
        if data['age'] < 18:
            raise serializers.ValidationError("Age should be between 18 and 90")
        if any([i in special_character for i in data['name']]):
            raise serializers.ValidationError("Name should not contain special character")
        
        return data

    
