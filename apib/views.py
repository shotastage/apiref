from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from apib.models import (
    APIB,
    AccessToken
)

# Create your views here.


class APIRef(View):

    @method_decorator(login_required)
    def get(self, request):


        session = APIB.objects.all().last()
    
        res = HttpResponse()
        res.write(session.content)

        return res

    def post(self, request):
        pass


class APITokenView(View):

    @method_decorator(login_required)
    def get(self, request):

        try:
            token = AccessToken.objects.all().last().token
        except:
            new = AccessToken.objects.create_token(
                user = request.user
            )
            new.save()
            token = AccessToken.objects.all().last().token

        context = {
            'access_token': token,
        }

        return render(request, "create_accessing_token.html", context)


    @method_decorator(login_required)
    def post(self, request):

        if request.POST["action"] == "regenerate":
            new = AccessToken.objects.create_token(
                user = request.user 
            )
            new.save()

        return redirect('/token/')
