from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Profile
from phonenumber_field.phonenumber import to_python
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ["first_name","last_name","phone_number","pk","role"]
        extra_kwargs = {
            "pk":{"read_only":True}
        }

    def validate_phone_number(self, value):
        # Convert to string if needed
        if isinstance(value, str) and value.startswith("0"):
            # Replace leading 0 with +213
            value = "+213" + value[1:]
        # Let django-phonenumber-field handle the rest
        return to_python(value)
    #def create(self, validated_data):
    #     user = self.context['request'].user
    #     profile = Profile.objects.create(user=user,**validated_data)
    #     return profile
    
class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","email","password","confirm_password",'profile','pk']
        extra_kwargs = {
            "password":{"write_only":True},
            "pk":{"read_only":True}
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
        user = User(**validated_data)
        user.set_password(validated_data.pop('password'))
        user.is_staff = True #remove later 
        user.save()
        Profile.objects.create(user=user,**profile_data)

        return user
