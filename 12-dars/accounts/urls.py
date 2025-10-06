from .views import RegisterView, LoginView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/', LoginView.as_view(), name='login')
]
