import datetime

from django.db import models
from django.utils import timezone

class Fortune(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.title