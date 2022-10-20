from django.db import models

class Loginapi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    password = models.TextField()

    class Meta:
        ordering = ['created']
