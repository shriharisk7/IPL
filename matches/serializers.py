from rest_framework import serializers
from .models import Match, Prediction

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'team1', 'team2', 'match_date', 'venue', 'status', 'winner', 'created_at', 'updated_at']

class PredictionSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    match_details = serializers.CharField(source='match.__str__', read_only=True)

    class Meta:
        model = Prediction
        fields = ['id', 'match', 'match_details', 'user', 'user_username', 'predicted_winner', 'points_earned', 'created_at']
        read_only_fields = ['points_earned'] 