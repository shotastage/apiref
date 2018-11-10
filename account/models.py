from django.db import models

# Create your models here.


class InvitationCode(models.Model):
  code = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255)
