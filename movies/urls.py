from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet, MovieScoreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'movie-score', MovieScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
