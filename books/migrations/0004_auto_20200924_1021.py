# Generated by Django 3.1.1 on 2020-09-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_userlibrary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='books',
            field=models.ManyToManyField(blank=True, to='books.Book'),
        ),
    ]
