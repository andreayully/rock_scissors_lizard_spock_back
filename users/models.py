from django.db import models


# Create your models here.

class GameUser(models.Model):
    """
    Model for users game
    """
    name = models.CharField(max_length=50)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
