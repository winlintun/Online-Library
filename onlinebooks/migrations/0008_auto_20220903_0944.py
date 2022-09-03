# Generated by Django 3.2 on 2022-09-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebooks', '0007_book_pdf_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_link',
            field=models.CharField(blank=True, max_length=2083, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_books',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
