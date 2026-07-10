from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Author, Book, BorrowHistory
from .forms import AuthorForm, BookForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer



# ---------------- HOME ----------------

def home(request):

    return render(
        request,
        "app/home.html"
    )



# ---------------- AUTHORS ----------------


def author_list(request):

    authors = Author.objects.all()

    return render(
        request,
        "app/author_list.html",
        {
            "authors": authors
        }
    )



def author_detail(request, id):

    author = get_object_or_404(
        Author,
        id=id
    )

    return render(
        request,
        "app/author_detail.html",
        {
            "author": author
        }
    )



@login_required
def add_author(request):

    form = AuthorForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Author added successfully!"
        )

        return redirect("authors")


    return render(
        request,
        "app/author_form.html",
        {
            "form": form
        }
    )



@login_required
def edit_author(request, id):

    author = get_object_or_404(
        Author,
        id=id
    )

    form = AuthorForm(
        request.POST or None,
        instance=author
    )


    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Author updated successfully!"
        )

        return redirect("authors")


    return render(
        request,
        "app/author_form.html",
        {
            "form": form
        }
    )



@login_required
def delete_author(request, id):

    author = get_object_or_404(
        Author,
        id=id
    )


    if request.method == "POST":

        author.delete()

        messages.success(
            request,
            "Author deleted successfully!"
        )

        return redirect("authors")


    return render(
        request,
        "app/author_confirm_delete.html",
        {
            "author": author
        }
    )





# ---------------- BOOKS ----------------


def book_list(request):

    books = Book.objects.all()


    search = request.GET.get("search")

    if search:

        books = books.filter(
            Q(title__icontains=search) |
            Q(author__name__icontains=search)
        )


    availability = request.GET.get("availability")


    if availability == "available":

        books = books.filter(
            copies_available__gt=0
        )


    elif availability == "unavailable":

        books = books.filter(
            copies_available=0
        )



    paginator = Paginator(
        books,
        5
    )


    page_number = request.GET.get("page")


    books = paginator.get_page(
        page_number
    )



    return render(
        request,
        "app/book_list.html",
        {
            "books": books,
            "search": search,
            "availability": availability
        }
    )





def book_detail(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    return render(
        request,
        "app/book_detail.html",
        {
            "book": book
        }
    )





@login_required
def add_book(request):

    form = BookForm(request.POST or None)


    if form.is_valid():

        form.save()


        messages.success(
            request,
            "Book added successfully!"
        )


        return redirect("books")


    return render(
        request,
        "app/book_form.html",
        {
            "form": form
        }
    )





@login_required
def edit_book(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    form = BookForm(
        request.POST or None,
        instance=book
    )


    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Book updated successfully!"
        )

        return redirect("books")



    return render(
        request,
        "app/book_form.html",
        {
            "form": form
        }
    )





@login_required
def delete_book(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    if request.method == "POST":

        book.delete()


        messages.success(
            request,
            "Book deleted successfully!"
        )


        return redirect("books")



    return render(
        request,
        "app/book_confirm_delete.html",
        {
            "book": book
        }
    )





# ---------------- BORROW BOOK ----------------


@login_required
def borrow_book(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    if book.copies_available > 0:


        book.copies_available -= 1

        book.save()



        BorrowHistory.objects.create(
            book=book,
            user=request.user
        )



        messages.success(
            request,
            "Book borrowed successfully!"
        )


    else:

        messages.error(
            request,
            "No copies available!"
        )


    return redirect(
        "book_detail",
        id=id
    )





# ---------------- RETURN BOOK ----------------


@login_required
def return_book(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )



    if book.copies_available < book.copies_total:


        book.copies_available += 1

        book.save()



        history = BorrowHistory.objects.filter(
            book=book,
            user=request.user,
            returned_date=None
        ).last()



        if history:

            history.returned_date = timezone.now()

            history.save()



        messages.success(
            request,
            "Book returned successfully!"
        )



    else:

        messages.error(
            request,
            "All copies are already available!"
        )



    return redirect(
        "book_detail",
        id=id
    )

# ---------------- BORROW HISTORY ----------------


@login_required
def borrow_history(request):

    history = BorrowHistory.objects.filter(
        user=request.user
    ).order_by(
        "-borrowed_date"
    )


    return render(
        request,
        "app/borrow_history.html",
        {
            "history": history
        }
    )

# ---------------- API ----------------


@api_view(["GET"])
def book_api(request):

    books = Book.objects.all()

    serializer = BookSerializer(
        books,
        many=True
    )

    return Response(
        serializer.data
    )




@api_view(["GET"])
def author_api(request):

    authors = Author.objects.all()

    serializer = AuthorSerializer(
        authors,
        many=True
    )

    return Response(
        serializer.data
    )

# ---------------- API DETAIL ----------------


@api_view(["GET"])
def book_detail_api(request, id):

    book = get_object_or_404(
        Book,
        id=id
    )


    serializer = BookSerializer(
        book
    )


    return Response(
        serializer.data
    )




@api_view(["GET"])
def author_detail_api(request, id):

    author = get_object_or_404(
        Author,
        id=id
    )


    serializer = AuthorSerializer(
        author
    )


    return Response(
        serializer.data
    )