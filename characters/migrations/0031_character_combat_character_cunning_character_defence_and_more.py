# Generated by Django 5.2.3 on 2025-07-08 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0030_character_agility'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='combat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='cunning',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='defence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='health',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='initiative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='lore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='luck',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='melee_to_hit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='range_to_hit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='sanity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='spirit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='willpower',
            field=models.IntegerField(default=0),
        ),
    ]
