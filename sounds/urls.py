from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sounds.views import SoundViewSet, SoundScoreViewSet

router = DefaultRouter()
router.register(r'sounds', SoundViewSet)
router.register(r'sound-score', SoundScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
