from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

class Stock(models.Model):
    date = models.DateField(max_length=200)
    open = models.CharField(max_length=200)
    high = models.CharField(max_length=200)
    low = models.CharField(max_length=200)
    close = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    adj = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    def __str__(self):
        return self.volume

