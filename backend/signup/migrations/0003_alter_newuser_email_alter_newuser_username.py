# Generated by Django 4.1.1 on 2022-09-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_newuser_email_alter_newuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email has already been registered.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'This username has already been taken.'}, max_length=120, unique=True),
        ),
    ]
