from django.views import View
from django.shortcuts import render, redirect
from .forms import UserCreateForm

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form" : create_form
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
        return render(request, 'accounts/login.html')