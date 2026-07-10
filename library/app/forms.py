from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:

        model = Author

        fields = "__all__"

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = "__all__"

        widgets = {
            "published_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "genres": forms.CheckboxSelectMultiple(),
        }