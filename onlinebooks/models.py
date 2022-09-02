from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField()
	slug_url = models.SlugField(max_length=200, null=True, blank=True, help_text="a-bite-of-python")
	book_link = models.CharField(max_length=2083)
	image = models.ImageField(default='../static/onlinebooks/img/default.png', upload_to="media")
	create_date = models.DateTimeField(default=timezone.now)
	upload_user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
