from django.conf.urls import url, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]