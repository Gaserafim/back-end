from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hqs.views import HQViewSet, HQScoreViewSet

router = DefaultRouter()
router.register(r'hq', HQViewSet)
router.register(r'hq-score', HQScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
