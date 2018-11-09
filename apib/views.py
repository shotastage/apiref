from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apib.models import APIB

# Create your views here.


class APIRef(View):

    @login_required
    def get(self, request):

        session = APIB.objects.latest()
    
        res = HttpResponse(mimetype="text/html")
        res.write(session.contents)

        return res

    def post(self, request):
        pass
