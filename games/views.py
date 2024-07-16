from games.models import Game, GameScore
from games.serializers import GameSerializer, GameScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminOrReadOnly]


class GameScoreViewSet(viewsets.ModelViewSet):
    queryset = GameScore.objects.all()
    serializer_class = GameScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        game_score = self.get_object()
        if game_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(game_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        game_score = self.get_object()
        if game_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(game_score)
        return Response(status=status.HTTP_204_NO_CONTENT)
