from django.urls import path
from apib.views import (
    APIRefFrame,
    APIHomeView,
    APITokenView,
    APISubmitView
)

urlpatterns = (
    path('', APIHomeView.as_view()),
    path('apiref_render/', APIRefFrame.as_view()),
    path('submit_compiled_blueprint/', APISubmitView.as_view()),
    path('token/', APITokenView.as_view()),
)
