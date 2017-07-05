from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username

# Create your models here.
