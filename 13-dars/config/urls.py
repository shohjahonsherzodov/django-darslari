from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('book/', include('book.urls')),
    path('accounts/', include('accounts.urls'))
]
