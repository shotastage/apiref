import secrets
from datetime import datetime
from django.db import models



class APIBManager(models.Manager):

    def submit_new(self, contents):
        new = self.create(
            content = contents
        )

        return new

class APIB(models.Model):
    division = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    is_disabled = models.BooleanField(default=False)

    objects = APIBManager()



class AccessTokenManager(models.Manager):

    def create_token(self, user):
        token = self.create(
            token = secrets.token_urlsafe(32),
            created_by = str(user),
        )

        return token


class AccessToken(models.Model):
    token = models.CharField(max_length = 255)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.CharField(max_length = 255)

    objects = AccessTokenManager()
