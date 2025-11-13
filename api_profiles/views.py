from django.shortcuts import render
from rest_framework.views import APIView #Handling manual HTTP requests
from rest_framework.response import Response #Handling the JSON output
from rest_framework import status #Handles the statuses for the requests
from rest_framework import viewsets #Automatically handles HTTP requests
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from api_profiles import serializers
from api_profiles import models #Import the models so we can create proifle
from api_profiles import permissions

#Example of how to use APIView :
class GreetingAPIView(APIView):
	#Creating manual HTTP Request using APIView for custom endpoints
	serializer_class = serializers.GreetingSerializer
	def get(self,request,format=None):
		list_of_strings = ["Hello this is the first string",
							"This is the second string that will be printed on GET request",
							"This is actually the final string that is in this list"]
		return Response({"Greeting":"Hey there!","message":list_of_strings})

	def post(self,request):
		#Create a hello message including the user's name
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hey, how you doing {name}'
			return Response({"messsage":message})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	#Example of how to use the other HTTP requests using APIView:
	def put(self,request,pk=None): #Primary key used as ID to update object by its id
		return Response({'HTTP Method':"PUT"})

	def patch(self,request,pk=None):
		return Response({'HTTP Method':"PATCH"})

	def delete(self,request,pk=None):
		return Response({'HTTP Method':"DELETE"})


#Example of how to use ViewSet :
class GreetingViewSet(viewsets.ViewSet):
	serializer_class = serializers.GreetingSerializer #We can use the same serializer from the APIView example
	def list(self,request): #GET HTTP request
		list_of_strings = ["This is another example of HTTP requests - this time using ViewSet",
						"We will print these lines on GET request",
						"This is the final string of the list that will be printed"]
		return Response({'message':"Hello,check out these strings:","strings":list_of_strings})

	def create(self,request): #POST HTTP request
		#Create a hello message including the user's name
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello, how you doing {name}'
			return Response({"response":message})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	#Example of how to use the other HTTP requests using ViewSet:
	def retrieve(self,request,pk=None): #GET HTTP Request
		return Response({'HTTP Method':"GET"})

	def update(self,request,pk=None): #PUT HTTP Method
		return Response({'HTTP Method':'PUT'})

	def partial_update(self,request,pk=None): #PATCH HTTP Method
		return Response({'HTTP Method':'PATCH'})
		
	def destroy(self,request,pk=None): #DELETE HTTP Method
		return Response({'HTTP Method':'DELETE'})


class CreateUserProfileViewSet(viewsets.ModelViewSet):
	#Handle creating and updating profiles
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all() #Default set of users
	permission_classes = (permissions.UpdateOnlyOwnProfile,)
	#Create a search bar
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email','username',) #User can be searched by these fields


class UserLoginAPIView(ObtainAuthToken):
	#Handle creating user authentication tokens
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
