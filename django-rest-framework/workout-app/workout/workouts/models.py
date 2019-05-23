from django.db import models
from django.conf import settings


class WorkoutQuerySet(models.QuerySet):
    pass

class WorkoutManager(models.Manager):
    def get_queryset(self):
        return WorkoutQuerySet(self.model, using=self._db)


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=125)
    sets = models.PositiveSmallIntegerField(blank=False)
    repetitions = models.PositiveSmallIntegerField(blank=False)
    load = models.PositiveSmallIntegerField(blank=False, default=0)
    rate_of_perceived_exertion = models.PositiveSmallIntegerField(blank=True, null=True)
    percent_of_one_rep_max = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = WorkoutManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Workout Post"
        verbose_name_plural = "Workout posts"

    @property
    def owner(self):
        return self.user