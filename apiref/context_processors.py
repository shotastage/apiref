from django.conf import settings


def site_common_text(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
    }
