import email
from unicodedata import name
from django.db import models

# Create your models here.


class NewUser(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(
        max_length=254, unique=True, error_messages={'unique': "This email has already been registered."})
    username = models.CharField(
        max_length=120, unique=True, error_messages={'unique': "This username has already been taken."})
    password = models.CharField(max_length=120)
    passrepeat = models.CharField(max_length=120)

    def __str__(self):
        return self.name
