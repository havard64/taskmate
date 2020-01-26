from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    goal = models.TextField(default="")
    notes = models.TextField(default="")

#    def __str__(self):
#       return self.task + " - " + str(self.done)


