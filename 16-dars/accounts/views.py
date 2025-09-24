from django.shortcuts import render
from .views import View
class LoginPageView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
class RegisterPageView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')