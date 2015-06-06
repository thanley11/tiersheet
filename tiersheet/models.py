from django.db import models


class Player(models.Model):

    POSITION_CHOICES = (
        ('QB', 'Quarterback'),
        ('RB', 'Runningback'),
        ('WR', 'Wide Receiver'),
        ('TE', 'Tight End'),
        ('DEF', 'Defense'),
        ('K', 'Kicker'),
    )

    name     = models.CharField(max_length=64, unique=True)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    bye      = models.IntegerField(null=True)
    url      = models.URLField(null=True,blank=True)
    order    = models.IntegerField(default=0)
    team     = models.CharField(max_length=3, null=True, default=None, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "players"

    def __unicode__(self):
        return self.name


class Rotoworld_Url(models.Model):

    name     = models.CharField(max_length=64, unique=True)
    roto_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name
