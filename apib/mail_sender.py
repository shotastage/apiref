from django.core.mail import send_mail
from typing import List


def construct_mail(sub: str, msg: str, to: List[str]):
    send_mail(
        sub,
        msg,
        'from@example.com',
        to,
        fail_silently=False)

def send_notification():
    pass
