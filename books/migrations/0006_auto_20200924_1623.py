# Generated by Django 3.1.1 on 2020-09-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200924_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
