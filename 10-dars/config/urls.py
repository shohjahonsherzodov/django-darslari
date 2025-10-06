from django.contrib import admin
from django.urls import path, include
from .views import landing_page, succes_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('succes_login/', succes_login, name='succes_login'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]
