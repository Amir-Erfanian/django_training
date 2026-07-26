from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .models import Book
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from .forms import BookForm
from .models import Book


class HomeView(TemplateView):

    template_name = "books/home.html"


class BookListView(ListView):

    model = Book

    context_object_name = "books"


class BookDetailView(DetailView):

    model = Book

    context_object_name = "book"

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")
    
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book-list")
    
class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book-list")