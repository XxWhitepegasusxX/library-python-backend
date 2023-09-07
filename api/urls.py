from django.urls import path
from .views import BookList, BookDetail, AuthorDetail, AuthorList, CategoryDetail, CategoryList

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<str:pk>/', BookDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('author/<str:pk>/', AuthorDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<str:pk>/', CategoryDetail.as_view()),
]
