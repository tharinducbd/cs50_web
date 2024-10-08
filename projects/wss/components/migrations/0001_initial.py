# Generated by Django 4.2.7 on 2024-02-09 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('color', models.CharField(max_length=12)),
                ('contruction_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tank_materials', to='components.material')),
            ],
        ),
    ]
