from django.urls import path
from apib.views import (
    APIRef,
    APITokenView
)

urlpatterns = (
    path('', APIRef.as_view()),
    path('token/', APITokenView.as_view()),
)
