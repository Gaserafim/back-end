from books.models import Book, BookScore
from books.serializers import BookSerializer, BookScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]


class BookScoreViewSet(viewsets.ModelViewSet):
    queryset = BookScore.objects.all()
    serializer_class = BookScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        book_score = self.get_object()
        if book_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(book_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request):
        book_score = self.get_object()
        if book_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(book_score)
        return Response(status=status.HTTP_204_NO_CONTENT)
