from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, BookScoreViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'book-score', BookScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
