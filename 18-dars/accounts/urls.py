from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView, profile_update

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile_update/', profile_update, name='profile_update')
]
