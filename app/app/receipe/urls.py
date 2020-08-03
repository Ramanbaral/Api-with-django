from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TagViewSet


router = DefaultRouter()
router.register('tags', TagViewSet)

urlpatterns = [
    path('tags/', TagViewSet.as_view(), name='tags')
]
