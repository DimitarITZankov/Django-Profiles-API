from django.urls import path, include
from api_profiles import views

urlpatterns = [
	path('hello-view/', views.GreetingAPIView.as_view())
]