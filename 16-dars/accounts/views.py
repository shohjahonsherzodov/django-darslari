from django.shortcuts import render
from django.views import View
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context = {
            "form":create_form
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
        form = UserLoginForm()
        return render(request, "accounts/login.html", {"form" : form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("landing_page")
        else:
            return render(request, "accounts/login.html", {"form" : form})