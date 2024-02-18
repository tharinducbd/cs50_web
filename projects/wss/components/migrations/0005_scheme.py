# Generated by Django 4.2.7 on 2024-02-12 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_tank_has_bulkmeter_tank_has_chamber_tank_has_washout_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(max_length=64)),
                ('district', models.CharField(max_length=32)),
                ('tanks', models.ManyToManyField(blank=True, related_name='schemes', to='components.tank')),
            ],
        ),
    ]