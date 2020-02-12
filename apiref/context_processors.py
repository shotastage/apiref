from django.conf import settings


def site_common_text(request):
    return {
        'APP_NAME': settings.SITE_NAME,
    }
