from django.db import models

class Game(models.Model):
    player_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'games'
