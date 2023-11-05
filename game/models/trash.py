from django.db import models

class Trash(models.Model):
    name = models.CharField(max_length=64)
    trash_category = models.ForeignKey('TrashCategory', on_delete=models.CASCADE)
    description = models.CharField(max_length=512)
    image_url = models.CharField(max_length=512)
    difficulty = models.IntegerField()

    class Meta:
        db_table = 'trashes'

class TrashCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

    class Meta:
        db_table = 'trash_category'
