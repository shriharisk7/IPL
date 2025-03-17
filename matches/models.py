from django.db import models
from django.utils import timezone

class Match(models.Model):
    MATCH_STATUS = (
        ('upcoming', 'Upcoming'),
        ('live', 'Live'),
        ('completed', 'Completed'),
    )
    
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=MATCH_STATUS, default='upcoming')
    winner = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.match_date.date()}"

class Prediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='predictions')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    predicted_winner = models.CharField(max_length=100)
    points_earned = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('match', 'user')

    def __str__(self):
        return f"{self.user.username}'s prediction for {self.match}"
