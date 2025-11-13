from django.shortcuts import render
from rest_framework.views import APIView #Handling manual HTTP requests
from rest_framework.response import Response #Handling the JSON output
from rest_framework import status #Handles the statuses for the requests
from api_profiles import serializers


class GreetingAPIView(APIView):
	#Creating manual HTTP Request using APIView for custom endpoints
	serializer_class = serializers.GreetingSerializer
	def get(self,request,format=None):
		list_of_strings = ["Hello this is the first string",
							"This is the second string that will be printed on GET request",
							"This is actually the final string that is in this list"]
		return Response({"Greeting":"Hey there!","message":list_of_strings})

	def post(self,request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hey, how you doing {name}'
			return Response({"messsage":message})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	#Example of how to use the other HTTP requests using APIView:
	def put(self,request.pk=None) #Primary key used as ID to update object by its ID
		return Response({'HTTP Method':"PUT"})

	def patch(self,request,pk=None):
		return Response({'HTTP Method':"PATCH"})

	def delete(self,request,pk=None):
		return Response({'HTTP Method':"DELETE"})
		
