from django.urls import path
from apib.views import (
    APIRefFrame,
    APIHomeView,
    APITokenView
)

urlpatterns = (
    path('', APIHomeView.as_view()),
    path('apiref_render/', APIRefFrame.as_view()),
    path('token/', APITokenView.as_view()),
)
