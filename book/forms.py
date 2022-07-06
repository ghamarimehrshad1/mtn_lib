from dataclasses import fields
from email.policy import default
from django import forms
from book.models import Comment,Book

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('title','content')


class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        exclude = ('user',)


class AdvanceSearch(forms.Form):
    book_name= forms.CharField(max_length=50,required=False)
    exact_book_name=forms.BooleanField(required=False)
    author_name= forms.CharField(max_length=50,required=False)
    publisher_name= forms.CharField(max_length=50,required=False)
