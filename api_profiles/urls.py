from django.urls import path, include
from api_profiles import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.GreetingViewSet,base_name='hello-viewset')

urlpatterns = [
	path('hello-view/', views.GreetingAPIView.as_view()),
	path('', include(router.urls)),
]
