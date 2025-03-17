from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Match, Prediction
from .serializers import MatchSerializer, PredictionSerializer

# Create your views here.

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Match.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        return queryset.order_by('match_date')

    @action(detail=True, methods=['post'])
    def predict(self, request, pk=None):
        match = self.get_object()
        if match.status != 'upcoming':
            return Response(
                {'error': 'Can only make predictions for upcoming matches'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        predicted_winner = request.data.get('predicted_winner')
        if not predicted_winner:
            return Response(
                {'error': 'Predicted winner is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        prediction, created = Prediction.objects.get_or_create(
            match=match,
            user=request.user,
            defaults={'predicted_winner': predicted_winner}
        )

        if not created:
            prediction.predicted_winner = predicted_winner
            prediction.save()

        serializer = PredictionSerializer(prediction)
        return Response(serializer.data)

class PredictionViewSet(viewsets.ModelViewSet):
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Prediction.objects.filter(user=self.request.user)
