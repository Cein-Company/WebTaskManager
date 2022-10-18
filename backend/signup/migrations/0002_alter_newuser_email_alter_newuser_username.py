# Generated by Django 4.1.1 on 2022-09-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]