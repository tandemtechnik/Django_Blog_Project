# Generated by Django 4.1.7 on 2023-04-19 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='img',
            new_name='image',
        ),
    ]
