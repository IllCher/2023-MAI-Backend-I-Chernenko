# Generated by Django 4.2 on 2023-04-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_director_options_alter_film_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='directiors',
            new_name='directors',
        ),
    ]