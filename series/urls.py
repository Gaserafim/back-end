from django.urls import path, include
from rest_framework.routers import DefaultRouter
from series.views import SeriesViewSet, SerieScoreViewSet

router = DefaultRouter()
router.register(r'series', SeriesViewSet)
router.register(r'serie-score', SerieScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
