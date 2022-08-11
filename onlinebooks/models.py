from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()
	cateogry = models.ManyToManyField('Category')
	slug_url = models.SlugField(max_length=200, null=True, blank=True, help_text="a-bite-of-python")
	book_link = models.CharField(max_length=2083)
	image = models.ImageField(upload_to='media/')
	create_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

