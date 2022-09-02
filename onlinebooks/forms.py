from django import forms
from .models import Book
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User


# class DateTimePickerInput(forms.DateTimeInput):
#     input_type = 'datetime'
#
#
# class BookForm(forms.Form):
#     title = forms.CharField(max_length=200, label="Book Name", required=True)
#     author = forms.CharField(label="Author", max_length=200, required=False)
#     description = forms.CharField(widget=forms.Textarea, required=False)
#     book_link = forms.URLField(required=True)
#     image = forms.ImageField()
#     create_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
#     upload_user = forms.ModelChoiceField(queryset=User.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super(BookForm, self).__init__(*args, **kwargs)
#
#         # add class to default html tags created by django
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
#
#         # add attribute to define acceptable file-type
#         self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"
#         self.fields['description'].widget.attrs['class'] = 'textarea--style-6'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'book_link', 'image', 'create_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        # add class to default html tags created by django
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        # add attribute to define acceptable file-type
        self.fields['image'].widget.attrs['accept'] = "image/png, image/gif, image/jpeg"
        self.fields['description'].widget.attrs['class'] = 'textarea--style-6'
