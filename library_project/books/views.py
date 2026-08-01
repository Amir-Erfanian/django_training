from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.core.cache import cache
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class HomeView(TemplateView):
    template_name = "books/home.html"


class BookListView(ListView):
    model = Book
    context_object_name = "books"


# class BookDetailView(DetailView):
#     model = Book
#     context_object_name = "book"


class BookDetailView(DetailView):

    model = Book
    context_object_name = "book"

    def get_object(self, queryset=None):

        book_id = self.kwargs.get("pk")

        cache_key = f"book_{book_id}"

        # Check Redis
        book = cache.get(cache_key)

        if book:
            print("Loaded from Redis")
            return book

        # If not in Redis, get from database
        book = super().get_object(queryset)

        # Store in Redis for 1 hour
        cache.set(cache_key, book, timeout=3600)

        print("Loaded from Database")

        return book


class BookCreateView(
    PermissionRequiredMixin,
    CreateView,
):
    permission_required = "books.add_book"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book-list")


class BookUpdateView(
    UserPassesTestMixin,
    UpdateView,
):

    model = Book
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)

        cache.delete(f"book_{self.object.id}")

        return response

    def test_func(self):
        return self.request.user.is_staff


class BookDeleteView(
    PermissionRequiredMixin,
    DeleteView,
):

    permission_required = "books.delete_book"
    model = Book
    success_url = reverse_lazy("book-list")

    def delete(self, request, *args, **kwargs):

        book = self.get_object()

        cache.delete(f"book_{book.id}")

        return super().delete(request, *args, **kwargs)
