# Generated by Django 5.2.3 on 2025-06-27 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_side_bag'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='side_bag',
            name='token',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='character_token', to='equipment.token'),
        ),
    ]
