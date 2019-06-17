from urllib.parse import quote
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from account.models import InvitationCode



class CodeGenerate(View):

    def get(self, request):
        return render(request, 'registration/code_result.html')


    @method_decorator(login_required)
    def post(self, request):

        user = request.POST["user"]
        email = request.POST["email"]
        passwd = request.POST["passwd"]
        passwd_confirm = request.POST["passwd_confirm"]


        if passwd == passwd_confirm:
            pass

        res = redirect("/register_new/")
        res['location'] += '?' "email=" + quote(email)

        return res
