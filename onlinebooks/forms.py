from django import forms
from .models import Book, Comment
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'book_link', 'pdf_books', 'image', 'create_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        # add class to default html tags created by django
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        # add attribute to define acceptable file-type
        self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"
        self.fields['description'].widget.attrs['class'] = 'textarea--style-6'
        self.fields['pdf_books'].widget.attrs['accept'] = ".pdf"



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'date_created', ]

    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['placeholder'] = 'Comment here !'
        self.fields['date_created'].widget.attrs['class'] = 'd-inline'