from django.urls import path
from . import views



urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),


    # Books
    path(
        "books/",
        views.book_list,
        name="books"
    ),

    path(
        "book/<int:id>/",
        views.book_detail,
        name="book_detail"
    ),

    path(
        "book/add/",
        views.add_book,
        name="add_book"
    ),

    path(
        "book/edit/<int:id>/",
        views.edit_book,
        name="edit_book"
    ),

    path(
        "book/delete/<int:id>/",
        views.delete_book,
        name="delete_book"
    ),


    path(
        "book/<int:id>/borrow/",
        views.borrow_book,
        name="borrow_book"
    ),


    path(
        "book/<int:id>/return/",
        views.return_book,
        name="return_book"
    ),



    # Authors

    path(
        "authors/",
        views.author_list,
        name="authors"
    ),


    path(
        "author/<int:id>/",
        views.author_detail,
        name="author_detail"
    ),


    path(
        "author/add/",
        views.add_author,
        name="add_author"
    ),


    path(
        "author/edit/<int:id>/",
        views.edit_author,
        name="edit_author"
    ),


    path(
        "author/delete/<int:id>/",
        views.delete_author,
        name="delete_author"
    ),

 
path(
    "borrow-history/",
    views.borrow_history,
    name="borrow_history"
),

path(
    "api/books/",
    views.book_api,
    name="book_api"
),


path(
    "api/authors/",
    views.author_api,
    name="author_api"
),

path(
    "api/books/<int:id>/",
    views.book_detail_api,
    name="book_detail_api"
),


path(
    "api/authors/<int:id>/",
    views.author_detail_api,
    name="author_detail_api"
),

]