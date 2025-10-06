from django.urls import path
from .views import BookView, BookDetailView


urlpatterns = [
    path('list/', BookView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail')
]
