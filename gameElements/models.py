from django.db import models
from users.models import GameUser
from django.utils import timezone


class GameElement(models.Model):
    """
    Model for game elements
    """
    name = models.CharField(max_length=50)
    beats = models.ManyToManyField("self", through='ElementBeat', related_name='elements', blank=True)

    def __str__(self):
        return self.name


class ElementBeat(models.Model):
    element = models.ForeignKey("GameElement", related_name="element_beats", on_delete=models.CASCADE)
    beat = models.ForeignKey("GameElement", related_name="beat", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.element} - {self.beat}'


class Match(models.Model):
    """
    Model for game
    """
    user_1 = models.ForeignKey(GameUser, on_delete=models.PROTECT, related_name='match_user_1')
    user_2 = models.ForeignKey(GameUser, on_delete=models.PROTECT, related_name='match_user_2')
    element_user_1 = models.ForeignKey(GameElement, on_delete=models.PROTECT, related_name='match_element_1',
                                       blank=True, null=True)
    element_user_2 = models.ForeignKey(GameElement, on_delete=models.PROTECT, related_name='match_element_2',
                                       blank=True, null=True)
    ts = models.DateTimeField(default=timezone.now)
    winner = models.ForeignKey(GameUser, on_delete=models.PROTECT, related_name='match_winner', blank=True, null=True)
