from django.db import models


class ClockConfig(models.Model):
    time = models.DateTimeField()
