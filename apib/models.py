from django.db import models

# Create your models here.


class APIB(models.Model):
    division = models.DateTimeField()
    content = models.TextField()
    is_disabled = models.BooleanField()
