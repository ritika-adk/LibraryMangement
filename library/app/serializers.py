from rest_framework import serializers

from .models import Book, Author



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author

        fields = "__all__"




class BookSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()


    class Meta:

        model = Book

        fields = [
            "id",
            "title",
            "author",
            "isbn",
            "published_date",
            "copies_total",
            "copies_available",
            "is_available",
        ]