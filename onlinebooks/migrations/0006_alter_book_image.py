# Generated by Django 3.2 on 2022-09-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebooks', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='../static/onlinebooks/img/default.png', upload_to='media/'),
        ),
    ]
