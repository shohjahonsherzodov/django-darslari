from django.contrib import admin
from django.urls import path, include
from config.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='homepage'),
    path('users/', include('users.urls'), name='users'),
]
