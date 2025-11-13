from django.urls import path, include
from api_profiles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.GreetingViewSet,base_name='hello-viewset')
router.register('register', views.CreateUserProfileViewSet) #Here no need of base_name because we have queryset,otherwise we will override the name

urlpatterns = [
	path('hello-view/', views.GreetingAPIView.as_view()),
	path('login/', views.UserLoginAPIView.as_view()),
	path('', include(router.urls)),
]
