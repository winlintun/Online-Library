# Generated by Django 3.2 on 2022-09-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebooks', '0006_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_books',
            field=models.FileField(default=1, upload_to='upload/'),
            preserve_default=False,
        ),
    ]
