# Generated by Django 5.2.3 on 2025-07-01 17:23

import equipment.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0024_per_adventure_per_fight_per_turn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='side_bag',
            options={'ordering': (equipment.models.Token,)},
        ),
    ]
