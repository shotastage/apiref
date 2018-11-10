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


        session = APIB.objects.all().last()
    
        res = HttpResponse()
        res.write(session.content)

        return res

    def post(self, request):
        pass


class APITokenView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, "create_accessing_token.html")
