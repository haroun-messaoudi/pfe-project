from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Profile
from phonenumber_field.phonenumber import to_python
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ["first_name","last_name","phone_number"]


    #def create(self, validated_data):
    #     user = self.context['request'].user
    #     profile = Profile.objects.create(user=user,**validated_data)
    #     return profile
    
class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username","email","password","confirm_password",'profile']
        extra_kwargs = {
            "password":{"write_only":True}
        }
    
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user,**profile_data)

        return user

    
