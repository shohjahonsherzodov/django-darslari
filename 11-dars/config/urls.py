from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls'), name='accounts'),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('book/', include('book.urls'), name='book')
]
