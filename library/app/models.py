from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):

    name = models.CharField(max_length=100)

    bio = models.TextField(
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )


    def __str__(self):

        return self.name


class Genre(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )
    
    genres = models.ManyToManyField(
    Genre,
    blank=True,
    verbose_name="Genre"
    )

    isbn = models.CharField(
        max_length=13,
        unique=True
    )


    published_date = models.DateField(
        blank=True,
        null=True
    )


    copies_total = models.PositiveIntegerField(
        default=1
    )


    copies_available = models.PositiveIntegerField(
        default=1
    )
    class Meta:

      ordering = ['title']



    @property
    def is_available(self):

        return self.copies_available > 0



    def __str__(self):

        return self.title
    



class BorrowHistory(models.Model):

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrow_history"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    borrowed_date = models.DateTimeField(
        auto_now_add=True
    )

    returned_date = models.DateTimeField(
        blank=True,
        null=True
    )


    def __str__(self):

        return f"{self.user.username} borrowed {self.book.title}"    