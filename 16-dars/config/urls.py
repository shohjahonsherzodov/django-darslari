from django.contrib import admin
from django.urls import path, include
from .views import landing_page, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('about/', about, name='about')
]
