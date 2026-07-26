from django.contrib import admin
from .models import Author, Book, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "price",
        "pages",
        "published_date",
    )

    list_filter = (
        "author",
        "categories",
    )

    search_fields = (
        "title",
        "author__name",
    )

    filter_horizontal = ("categories",)
