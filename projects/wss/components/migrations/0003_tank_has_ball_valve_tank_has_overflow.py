# Generated by Django 4.2.7 on 2024-02-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_rename_contruction_material_tank_construction_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='tank',
            name='has_ball_valve',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tank',
            name='has_overflow',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]