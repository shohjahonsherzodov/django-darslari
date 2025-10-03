from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm    
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


class RegisterView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
        return render(request, "accounts/register.html", {"form": form})
class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm
        context = {
            'form' : login_form
        }
        return render(request, 'accounts/login.html', context)
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga muvaffaqiyatli kirdingiz")
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'login_form' : login_form})
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/profile.html', {'user' : request.user })
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan muvaffaqiyatli chiqdingiz")
        return redirect("home")
    
@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) 
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'accounts/profile_update.html', context)
 