from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from apib.models import (
    APIB,
    AccessToken
)
from apib.htmlstring import stylesheet, navbar

# Create your views here.


class APIHomeView(View):
    @method_decorator(login_required)
    def get(self, request):

        return render(request, "home.html")

class APIRefFrame(View):

    @method_decorator(login_required)
    def get(self, request):

        content = APIB.objects.all().last().content
    
        res = HttpResponse()
        res.write(content)

        return res



class APISubmitView(View):

    def post(self, request):
        token = request.META["HTTP_APIREF_TOKEN"]
        body = request.body.decode('utf-8')


        if AccessToken.objects.all().last().token == token:
            new = APIB.objects.submit_new(
                contents = str(body)
            )
            new.save()


            return HttpResponse("Successful created new api doc!", status=201)
        else:
            return HttpResponse("Access token is wrong!", status=403)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(APISubmitView, self).dispatch(*args, **kwargs)



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
