from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('añadir/libro', views.BookCreate.as_view(), name="añadir"),
    path('eliminar/<int:pk>/', views.BookDelete.as_view(), name='eliminar'),
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>/', views.return_book, name='return_book'),
]
