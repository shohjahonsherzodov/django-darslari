from django.urls import path
from .views import RegisterView, LoginPageView

app_name = 'accounts'
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginPageView.as_view(), name="login"),
]
