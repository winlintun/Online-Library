from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book, Category
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import BookForm


def home(request):
	book = Book.objects.all()
	contenxt = {'books': book}

	return render(request, 'onlinebooks/index.html', contenxt)


def detail(request, pk, slug_text):

	my_book = Book.objects.get(id=pk)
	my_cateogry = my_book.cateogry.all

	unique_slug = slug_text

	all_book = Book.objects.all()[::-5]

	contenxt = {"books": unique_slug,
				'my_book': my_book,
				'all_book':all_book,
				'my_cateogry':my_cateogry}

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
	user = User.objects.get(id=pk)
	categories = Category.objects.all()
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		description = request.POST['description']
		cateogry = request.POST['cateogry']
		book_link = request.POST['book_link']
		image = request.POST['image']  # 1 item

		my_category = set()
		for i in cateogry:
			my_category.add(i)
		print(my_category)
		mybook = Book(title=title, author=author, description=description, book_link=book_link, image=image)
		mybook.save()
		return redirect("onlinebooks:home")

	context = {'categories': categories}

	return render(request, 'onlinebooks/upload-form.html', context)

""" 
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			user_form = form.save(commit=False)
			title = form.cleaned_data.get('title')
			author = form.cleaned_data.get('author')
			cateogry = form.cleaned_data.get('cateogry')
			book_link = form.cleaned_data.get('book_link')
			image = form.cleaned_data.get('image')
			form.save()

			return redirect("onlinebooks:home")
	else:
		form = BookForm()
		#return redirect("onlinebooks:home")

	context = {"form": form}
	"""