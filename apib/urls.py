from django.urls import path
from apib.views import (
    APIRefFrame,
    APIHomeView,
    APITokenView,
    APISubmitView,
    MailSenderView
)

urlpatterns = (
    path('', APIHomeView.as_view()),
    path('apiref_render/', APIRefFrame.as_view()),
    path('submit_compiled_blueprint/', APISubmitView.as_view()),
    path('test_mail_sender/', MailSenderView.as_view()),
    path('token/', APITokenView.as_view()),
)
