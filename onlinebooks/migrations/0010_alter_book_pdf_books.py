# Generated by Django 3.2 on 2022-09-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebooks', '0009_alter_book_pdf_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf_books',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]