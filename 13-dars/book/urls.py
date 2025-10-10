from django.urls import path
from .views import BookListView, BookDetailView

app_name = 'book'

urlpatterns = [
    path('list/', BookListView.as_view, name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail')
]
