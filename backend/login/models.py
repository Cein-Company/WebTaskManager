from contextlib import nullcontext
from select import select
from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=120)

    # checking if user is in database
    @classmethod
    def check_user(cls, username):
        return cls.objects.filter(username=username).exists()

    # adding user to database
    @classmethod
    def add_user(cls, username):
        return cls.objects.create(username=username)

    password = models.CharField(max_length=120)

    # chcking if password is correct
    @classmethod
    def check_password(cls, username, password):
        return cls.objects.filter(username=username, password=password).exists()

    # adding password to database
    @classmethod
    def add_password(cls, username, password):
        return cls.objects.filter(username=username).update(password=password)

    def __str__(self):
        return self.username
