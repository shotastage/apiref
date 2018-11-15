from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from typing import List


def construct_mail(sub: str, msg: str, to: List[str]):
    send_mail(
        sub,
        msg,
        "APIRef <" + settings.EMAIL_FROM_ADDRESS + ">",
        to,
        fail_silently=False)

def send_notification(request):
    construct_mail(
        'API references update notification',
        '''
Your API document has been updated!
See or reload {0}://{1}

Thank you,

APIRef - API Document Server for CI
        '''.format(request.scheme, request.META.HTTP_HOST),
        get_all_username()
    )


def get_all_username():
    return User.objects.all().email
