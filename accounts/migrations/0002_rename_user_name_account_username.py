# Generated by Django 4.1.5 on 2023-01-03 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]
