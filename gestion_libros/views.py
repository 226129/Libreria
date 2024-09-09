from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', {'books': books})


def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.status == 'disponible':
        book.status = 'prestado'
        book.borrowed_by.add(request.user)
        book.save()
    return redirect('book_list')


def return_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.status == 'prestado' and request.user in book.borrowed_by.all():
        book.status = 'disponible'
        book.borrowed_by.remove(request.user)
        book.save()
    return redirect('book_list')


class BookCreate(CreateView):
    model = Book
    template_name = 'añadir.html'
    fields = ["title", "author", "pub_date"]
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    template_name = 'eliminar.html'
    success_url = reverse_lazy('book_list')
