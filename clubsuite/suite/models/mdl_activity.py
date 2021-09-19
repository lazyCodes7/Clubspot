from django.db import models
from django.utils import timezone

class Activity(models.Model):
    activity = models.TextField(default="",null=True)


    def __str__(self):
        return self.activity