from django.contrib import admin
from django.urls import path, include
from .views import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('', home, name='home'),
    path('about/', about, name='about'),
]
