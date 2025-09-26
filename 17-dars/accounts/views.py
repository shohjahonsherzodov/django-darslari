from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin 

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context = {
            'form' : create_form
        }
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email
        )

        user.set_password(password)
        user.save()

        return redirect('accounts:login')

class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, "accounts/login.html", {"login_form" : login_form})
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga muvvafaqiyatli kirdingiz")
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"login_form" : login_form})
        
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "accounts/profil.html", {"accounts:request":"accounts"})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan muvaffaqiyatli chiqdingiz!")
        return redirect("home")