import random, string
from urllib.parse import quote
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from account.models import InvitationCode



class CodeGenerate(View):

    @method_decorator(login_required)
    def get(self, request):

        res = None

        try:
            param = request.GET['email']
        except:
            param = None

        if param is not None:

            context = {
                'mail': param,
                'code': InvitationCode.objects.filter(email=param).last().code
            }


            res = render(request, 'registration/code_result.html', context)
        else:
            res = render(request, 'registration/code_gen.html')

        return res


    @method_decorator(login_required)
    def post(self, request):

        email = request.POST["email"]

        InvitationCode.objects.create_code(email)


        res = redirect("/register_new/")
        res['location'] += '?' "email=" + quote(email)

        return res


class CodeCheck(View):

    def get(self, request):
        return render(request, 'registration/code_check.html')

    def post(self, request):

        data = request.POST["verification_code"]

        codes = InvitationCode.objects.filter(code=data).first()

        if codes is None:
            context = {
                'error_msg': "Verification code is wrong!",
            }

            return render(request, 'registration/code_check.html', context)
        else:
            codes.is_activated = True
            codes.save()


        res = redirect('basic_profile/')
        res['location'] += '?' "email=" + quote(codes.email)

        return res



class RegisterView(View):

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
