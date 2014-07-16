from django.db import models

# Create your models here.
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
    bye      = models.IntegerField(default=0)
    url      = models.URLField()
    order    = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "players"

    def __unicode__(self):
        return self.name


