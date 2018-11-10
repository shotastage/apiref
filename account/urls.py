from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import CustomLoginView


urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view()),
)
