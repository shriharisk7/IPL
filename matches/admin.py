from django.contrib import admin
from .models import Match, Prediction

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'match_date', 'venue', 'status', 'winner')
    list_filter = ('status', 'match_date')
    search_fields = ('team1', 'team2', 'venue')

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('match', 'user', 'predicted_winner', 'points_earned')
    list_filter = ('points_earned', 'created_at')
    search_fields = ('user__username', 'predicted_winner')
