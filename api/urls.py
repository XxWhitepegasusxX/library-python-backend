from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<str:pk>/', BookDetail.as_view())
]
