# Generated by Django 3.2.8 on 2021-11-03 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_auto_20211103_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]