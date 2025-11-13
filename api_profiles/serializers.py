from rest_framework import serializers
from api_profiles import models

class GreetingSerializer(serializers.Serializer):
	#Setting up the serializer for the greeting function on POST request
	name = serializers.CharField(max_length=100)


class UserProfileSerializer(serializers.ModelSerializer):
	#Serializes a user profile object
	class Meta:
		model = models.UserProfile
		fields = ('id','username','name','email','password')
		#We create extra keyword arguments for the field password
		extra_kwargs = {
			'password':{
				'write_only':True,
				'style':{'input_type':'password'}
			}
		}

#We need to override the basic functions,otherwise it will store the password as cleartext in database which is big secure issue :
	def create(self,validated_data):
		#Create and return a new user
		user = models.UserProfile.objects.create_user(
			username=validated_data['username'],
			name=validated_data['name'],
			email=validated_data['email'],
			password=validated_data['password']
			)
		return user
		
#We do the same this here, after updating it will save it as cleartext,so we override it :
	def update(self,instance,validated_data):
		#Handle updating user account
		if 'password' in validated_data:
			password = validated_data.pop('password')
			instance.set_password(password)
		return super().update(instance,validated_data)


