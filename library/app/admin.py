from django.contrib import admin
from .models import Author, Book, Genre ,BorrowHistory




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "date_of_birth",
    )



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "isbn",
        "copies_total",
        "copies_available",
        "availability_status",
    )


    def availability_status(self, obj):

        if obj.is_available:
            return "Available"

        return "Not Available"


    availability_status.short_description = "Status"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
    )  

@admin.register(BorrowHistory)
class BorrowHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "book",
        "user",
        "borrowed_date",
        "returned_date",
    )


    list_filter = (
        "returned_date",
        "borrowed_date",
    )      