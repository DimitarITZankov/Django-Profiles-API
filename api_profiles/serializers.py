from rest_framework import serializers

class GreetingSerializer(serializers.Serializer):
	#Setting up the serializer for the greeting function on POST request
	name = serializers.CharField(max_length=100)
