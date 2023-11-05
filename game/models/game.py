from django.db import models

class Game(models.Model):
    player_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'games'

class Record(models.Model):
    game_id = models.ForeignKey('Game', on_delete=models.CASCADE)
    trash_id = models.ForeignKey('Trash', on_delete=models.CASCADE)
    is_answer = models.BooleanField(null=True)

    class Meta:
        db_table = 'records'