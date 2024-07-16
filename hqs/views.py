from hqs.models import HQ, HQScore
from hqs.serializers import HQSerializer, HQScoreSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from setup.permissions import IsAdminOrReadOnly

class HQViewSet(viewsets.ModelViewSet):
    queryset = HQ.objects.all()
    serializer_class = HQSerializer
    permission_classes = [IsAdminOrReadOnly]


class HQScoreViewSet(viewsets.ModelViewSet):
    queryset = HQScore.objects.all()
    serializer_class = HQScoreSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        hq_score = self.get_object()
        if hq_score.user != request.user:
            return Response({"detail": "You do not have permission to update this review."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(hq_score, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request):
        hq_score = self.get_object()
        if hq_score.user != request.user:
            return Response({"detail": "You do not have permission to delete this review."}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(hq_score)
        return Response(status=status.HTTP_204_NO_CONTENT)
