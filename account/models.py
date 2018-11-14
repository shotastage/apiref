import random, string
from django.db import models




class InvitationCodeManager(models.Manager):
    def create_code(self, email):
        code = self.create(
          code = self.gen_invitation_code(),
          email = email
        )

        return code

    def gen_invitation_code(self) -> str:
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(6)]
        return ''.join(randlst)


class InvitationCode(models.Model):
    code = models.CharField(max_length = 10, unique=True)
    email = models.CharField(max_length = 255, unique=True)
    is_activated = models.BooleanField(default=False)

    objects = InvitationCodeManager()
