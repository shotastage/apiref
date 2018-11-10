import random, string
from urllib.parse import quote

from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from account.models import InvitationCode



class CodeCheck(View):

    def get(self, request):
        return render(request, 'registration/code_check.html')

    def post(self, request):
        
        data = request.POST["username"]

        codes = InvitationCode.objects.filter(code=data).first()

        if codes is None:
            print("Your invitation code is wrong!")
        else:
            codes.is_activated = True
            codes.save()


        res = redirect('basic_profile/')
        res['location'] += '?' "email=" + quote(codes.email)

        return res


class RegisterView(View):

    def gen_invitation_code(self) -> str:
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(6)]
        return ''.join(randlst)


    def get(self, request):

        context = {
            'mail': request.GET['email'],
        }

        return render(request, 'registration/register.html', context)

    def post(self, request):
        
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]


        sess = InvitationCode.objects.filter(email=email).first()

        if sess.is_activated:
            new = User.objects.create_user(
                username = username,
                password = password,
                email = email,
            )
            new.save()
        else:
            print("This email account is not activated!")


        return redirect('/login/')
