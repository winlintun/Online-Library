# Generated by Django 4.1 on 2022-09-01 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('slug_url', models.SlugField(blank=True, help_text='a-bite-of-python', max_length=200, null=True)),
                ('book_link', models.CharField(max_length=2083)),
                ('image', models.ImageField(default='../static/onlinebooks/img/default.png', upload_to='../onlinebooks/img/')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
