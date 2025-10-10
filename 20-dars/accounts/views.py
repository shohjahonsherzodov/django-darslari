from django.shortcuts import render, redirect
from .forms import UserCreateForm   
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserUpdateForm




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
class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self,request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request,'accounts/profile_update.html', {"form":user_update_form})
    
    def post(self,request):
        user_update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,"Profile muvaffaqiyatli yangilandi!")

            return redirect("accounts:profile")
        
        return render(request,'accounts/profile_update.html', {"update_form":user_update_form})

 