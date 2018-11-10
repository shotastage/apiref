import random, string
from django.db import models



class InvitationCode(models.Model):
  code = models.CharField(max_length = 10)
  email = models.CharField(max_length = 255)
  is_activated = models.BooleanField(default=False)
