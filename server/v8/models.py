from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cartoon(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    url = models.URLField()

class Episode(models.Model):
    cartoon = models.CharField(max_length=50)
    title = models.CharField(max_length=50, primary_key=True)
    url = models.CharField(max_length=300)