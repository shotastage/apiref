from django.contrib import admin
from apib.models import (
    APIB,
    AccessToken
)


admin.site.register(APIB)
admin.site.register(AccessToken)
