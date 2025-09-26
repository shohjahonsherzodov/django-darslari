from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("logout/", LogoutView.as_view(), name='logout')
]
