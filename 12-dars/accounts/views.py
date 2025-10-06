from django.shortcuts import render, redirect
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views import View

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'create_form' : create_form
        }
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        create_form = UserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('accounts:login')
        else:
            context = {
                'create_form' : create_form
            }
            return redirect(request, 'accounts/register.html', context)
class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form' : login_form 
        }
        return render(request, 'accounts/login.html', context)
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing_page')
        else:
            context = {
                'login_form' : login_form
            }
            return render(request, 'accounts/login.html', context)