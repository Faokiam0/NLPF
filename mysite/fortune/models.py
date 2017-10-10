import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime 

class Fortune(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="anon")
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(default = datetime.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.title