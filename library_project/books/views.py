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


class BookDetailView(DetailView):

    model = Book

    context_object_name = "book"


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
    def test_func(self):
        return self.request.user.is_staff


class BookDeleteView(
    PermissionRequiredMixin,
    DeleteView,
):
    permission_required = "books.delete_book"
    model = Book
    success_url = reverse_lazy("book-list")