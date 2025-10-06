from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User  
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context = {
            "form":create_form
        }
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        create_form = UserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('accounts:login')
        else:
            context = {
                'form' : create_form
            }
            return render(request, 'accounts/register.html', context)
    
class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, "accounts/login.html", {"login_form" : login_form})
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("succes_login")
        else:
            return render(request, "accounts/login.html", {"login_form" : login_form})