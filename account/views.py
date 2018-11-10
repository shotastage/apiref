import random, string
from django.views.generic import View
from django.shortcuts import render, redirect
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


        return redirect('basic_profile/')


class RegisterView(View):

    def gen_invitation_code(self) -> str:
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(6)]
        return ''.join(randlst)


    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        pass
