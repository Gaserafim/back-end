from rest_framework import viewsets
from movies.models import Movie, MovieScore
from movies.serializers import MovieSerializer, MovieScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]


class MovieScoreViewSet(viewsets.ModelViewSet):
    queryset = MovieScore.objects.all()
    serializer_class = MovieScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        movie_score = self.get_object()
        if movie_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(movie_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request):
        movie_score = self.get_object()
        if movie_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(movie_score)
        return Response(status=status.HTTP_204_NO_CONTENT)