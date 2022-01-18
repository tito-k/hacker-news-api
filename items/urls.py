from django.urls import path, include
from rest_framework import routers

from .views import BaseViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('latest/', BaseViewSet.latest_news),
    path('create/', BaseViewSet.create_news)
]
