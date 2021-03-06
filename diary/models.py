from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Diary(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    goal = models.TextField(null=True, blank=True, default="")
    notes = models.TextField(null=True, blank=True, default="")
    date = models.DateField(default=datetime.now, blank=False)
    feelgood = models.CharField(null=True, max_length=30, default="Fantastic")
    productivity = models.CharField(null=True, max_length=30, default="Fantastic")
    metime = models.CharField(null=True, max_length=30, default="Fantastic")
    fftime = models.CharField(null=True, max_length=30, default="Fantastic")
    image = models.ImageField(upload_to='diary_image', blank=True, null=True)
    class Meta:
        unique_together = (("manage", "date"),)





#    def __str__(self):
#       return self.task + " - " + str(self.done)
