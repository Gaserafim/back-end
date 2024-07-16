from sounds.models import Sound, SoundScore
from sounds.serializers import SoundSerializer, SoundScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
    permission_classes = [IsAdminOrReadOnly]


class SoundScoreViewSet(viewsets.ModelViewSet):
    queryset = SoundScore.objects.all()
    serializer_class = SoundScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        sound_score = self.get_object()
        if sound_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(sound_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request):
        sound_score = self.get_object()
        if sound_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(sound_score)
        return Response(status=status.HTTP_204_NO_CONTENT)
