from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import BookForm
from django.utils.text import slugify


def home(request):
	book = Book.objects.all()
	contenxt = {'books': book}

	return render(request, 'onlinebooks/index.html', contenxt)


def detail(request, pk, slug_text):

	my_book = Book.objects.get(id=pk)

	unique_slug = slug_text

	all_book = Book.objects.all()[::-5]

	contenxt = {"books": unique_slug,
				'my_book': my_book,
				'all_book':all_book}

	return render(request, 'onlinebooks/items.html', contenxt)


def UserLogin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("onlinebooks:home")
		else:
			messages.info(request, "wrong username and password.")
			return redirect("onlinebooks:home")
	return render(request, 'onlinebooks/login.html')


def UserRegister(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password1 = request.POST['password1']
		if password == password1:
			if User.objects.filter(username=username).exists():
				messages.info(request, "Your username is already used.")
				return redirect("onlinebooks:register")
			if User.objects.filter(email=email).exists():
				messages.info(request, "Your email is already used.")
				return redirect("onlinebooks:register")
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect("onlinebooks:home")
	return render(request, 'onlinebooks/register.html')


def UserLogout(request):
	logout(request)
	return redirect("onlinebooks:home")


def content_form(request, pk):
	user = User.objects.get(pk=pk)
	if request.method == "POST":
		form = BookForm(request.POST, instance=user)
		if form.is_valid():
			title = form.cleaned_data['title']
			author = form.cleaned_data['author']
			description = form.cleaned_data['description']
			slug_url = slugify(title)
			book_link = form.cleaned_data['book_link']
			image = form.cleaned_data['image']
			create_date = form.cleaned_data['create_date']

			book = Book.objects.create(title=title, author=author, description=description, slug_url=slug_url, book_link=book_link, image=image, create_date=create_date, upload_user=user)
			book.save()
			return redirect("onlinebooks:home")
	else:
		form = BookForm()
	context = {
		'form': form,
	}

	return render(request, 'onlinebooks/upload-form.html', context)