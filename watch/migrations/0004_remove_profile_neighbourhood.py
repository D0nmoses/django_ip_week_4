# Generated by Django 3.2.8 on 2021-11-03 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0003_rename_username_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
    ]
