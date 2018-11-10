from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import (
    CodeCheck,
    RegisterView
)


urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view()),
    path('register/', CodeCheck.as_view()),
    path('register/basic_profile/', RegisterView.as_view()),
)
