from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='landing_page'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('book/', include('book.urls'), name='book'),
]
