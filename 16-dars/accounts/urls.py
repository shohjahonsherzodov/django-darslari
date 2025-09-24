from .views import LoginPageView, RegisterPageView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register')
]
