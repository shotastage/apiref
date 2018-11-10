import secrets
from datetime import datetime
from django.db import models


class APIB(models.Model):
    division = models.DateTimeField()
    content = models.TextField()
    is_disabled = models.BooleanField()



class AccessTokenManager(models.Manager):

    def create_token(self, user):
        token = self.create(
            token = secrets.token_hex(),
            user = user,
        )

        return token


class AccessToken(models.Model):
    token = models.CharField(max_length = 255)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.CharField(max_length = 255)

    objects = AccessTokenManager()
