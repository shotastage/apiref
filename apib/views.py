from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from apib.models import APIB

# Create your views here.


class APIRef(View):

    @method_decorator(login_required)
    def get(self, request):


        ##session = APIB.objects.latest()
    
        res = HttpResponse()
        res.write("""
        <!doctype html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>SSS</title>
        </head>
        <body>
        <h1>HELLO!</h1>
        </body>
        </html>
        """)

        return res

    def post(self, request):
        pass
