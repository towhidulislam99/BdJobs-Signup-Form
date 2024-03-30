from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    # skills = SkillsSerializer()
    # country = CountrySerializer()
    # Explicitly define password and confirm_password fields
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserRegistration
        fields = '__all__'

    def validate(self, data):
        # Check if password and confirm_password match
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"non_field_errors": ["Password and Confirm Password must match"]})
        
        # Hash the password
        data['password'] = make_password(data['password'])
        
        return data

    def create(self, validated_data):
        # Remove confirm_password from validated data before saving
        validated_data.pop('confirm_password', None)
        
        return super().create(validated_data)

