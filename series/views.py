from series.models import Series, SerieScore
from series.serializers import SeriesSerializer, SerieScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminOrReadOnly]


class SerieScoreViewSet(viewsets.ModelViewSet):
    queryset = SerieScore.objects.all()
    serializer_class = SerieScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        serie_score = self.get_object()
        if serie_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(serie_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request):
        serie_score = self.get_object()
        if serie_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(serie_score)
        return Response(status=status.HTTP_204_NO_CONTENT)