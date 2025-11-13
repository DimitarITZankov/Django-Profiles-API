from rest_framework import serializers
from api_profiles import models


class GreetingSerializer(serializers.Serializer):
    # Setting up the serializer for the greeting function on POST request
    name = serializers.CharField(max_length=100)


class UserProfileSerializer(serializers.ModelSerializer):
    # Serializes a user profile object

    class Meta:
        model = models.UserProfile
        # Fields to include in the API responses and forms
        fields = ('id', 'username', 'email', 'name', 'password')
        # We create extra keyword arguments for the password field
        extra_kwargs = {
            'password': {
                'write_only': True,  # password will not be included in GET responses
                'style': {'input_type': 'password'}  # hides input in browsable API
            }
        }

    # We need to override the basic functions; otherwise it will store the password as cleartext
    def create(self, validated_data):
        # Create and return a new user
        user = models.UserProfile.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']  # hashed inside create_user()
        )
        return user

    # We do the same here; after updating, it will save the password as cleartext if we don't override it
    def update(self, instance, validated_data):
        # Handle updating user account
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)  # hash the password before saving
        return super().update(instance, validated_data)
