from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

# Create your views here.


class APIRef(View):

    @login_required
    def get(self, request):
        pass

    def post(self, request):
        pass
