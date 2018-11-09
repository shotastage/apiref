from django.urls import path
from django.contrib.auth.views import LogoutView
from account.views import CustomLoginView


urlpatterns = (
    path('login/', CustomLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
)
