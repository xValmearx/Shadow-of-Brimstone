# Generated by Django 5.2.3 on 2025-06-14 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_alter_character_character_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passive_Buff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('assigned_to_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passive_buff', to='characters.character')),
            ],
        ),
    ]
