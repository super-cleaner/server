from django.db import models
from game.models import Game, Trash

class Record(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    is_answer = models.BooleanField(null=True)

    class Meta:
        db_table = 'records'