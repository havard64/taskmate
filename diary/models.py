from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Diary(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    goal = models.TextField(default="")
    notes = models.TextField(default="")
    date = models.DateField(primary_key=True, default=datetime.now, blank=False)

#    def __str__(self):
#       return self.task + " - " + str(self.done)


