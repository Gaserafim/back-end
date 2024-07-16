from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from books.views import BookViewSet, BookScoreViewSet
from games.views import GameViewSet, GameScoreViewSet
from hqs.views import HQViewSet, HQScoreViewSet
from movies.views import MovieViewSet, MovieScoreViewSet
from series.views import SeriesViewSet, SerieScoreViewSet
from sounds.views import SoundViewSet, SoundScoreViewSet

router = SimpleRouter()
router.register(r'books', BookViewSet)
router.register(r'book-score', BookScoreViewSet)
router.register(r'games', GameViewSet)
router.register(r'game-score', GameScoreViewSet)
router.register(r'hq', HQViewSet)
router.register(r'hq-score', HQScoreViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'movie-score', MovieScoreViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'serie-score', SerieScoreViewSet)
router.register(r'sounds', SoundViewSet)
router.register(r'sound-score', SoundScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', include('users.urls')),
    path('', include(router.urls)),
]
