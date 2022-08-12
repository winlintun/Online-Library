from django.forms import ModelForm
from .models import Book, Category
from django import forms


# class BookForm(ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = ['title', 'author', 'description', 'book_link', 'image' ]


class BookForm(forms.Form):
	title = forms.CharField(max_length=200, required=True)
	author = forms.CharField(max_length=200, required=False)
	description = forms.CharField(widget=forms.Textarea)
	cateogry = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
	book_link = forms.CharField(max_length=200, required=True)
	image = forms.FileField()
