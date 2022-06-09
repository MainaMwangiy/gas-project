from django.db import models
from django.forms import CharField

# Create your models here.
class Gas(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    