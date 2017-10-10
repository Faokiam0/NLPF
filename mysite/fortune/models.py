import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Fortune(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(default = datetime.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.title