from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewSet, GameScoreViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'game-score', GameScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
