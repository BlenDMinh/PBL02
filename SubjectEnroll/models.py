from operator import mod
from django.db import models

# Create your models here.
class TestData(models.Model):
    word = models.TextField(default='hello')