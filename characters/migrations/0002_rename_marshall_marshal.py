# Generated by Django 5.2.3 on 2025-06-11 23:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marshall',
            new_name='Marshal',
        ),
    ]
