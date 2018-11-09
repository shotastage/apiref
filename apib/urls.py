from django.urls import path
from apib.views import APIRef

urlpatterns = (
    path('', APIRef.as_view()),
)
