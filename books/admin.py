from django.contrib import admin
from books.models import Book, BookScore


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )

    readonly_fields = ["rating",]

admin.site.register(Book, BooksAdmin)


class BookScoreAdmin(admin.ModelAdmin):
    list_display = ("book",)

admin.site.register(BookScore, BookScoreAdmin)
