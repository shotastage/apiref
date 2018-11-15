from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from typing import List


def construct_mail(sub: str, msg: str, to: List[str]):
    send_mail(
        sub,
        msg,
        settings.EMAIL_FROM_ADDRESS,
        to,
        fail_silently=False)

def send_notification():
    construct_mail(
        'API references',
        '''
        ''',
        get_all_username()
    )


def get_all_username():
    return User.objects.all().email
