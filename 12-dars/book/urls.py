from django.urls import path
from .views import BookView, BookDetail

urlpatterns = [
    path('', BookView.as_view(), name='list'),
    path('<int:id>/', BookDetail.as_view(), name='detail')
]