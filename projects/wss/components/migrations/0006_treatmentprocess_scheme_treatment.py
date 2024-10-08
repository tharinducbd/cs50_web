# Generated by Django 4.2.7 on 2024-02-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_scheme'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('PT_INT', 'Pre-treatment: Intake'), ('PT_WTP', 'Pre-treatment: WTP'), ('AE', 'Aeration'), ('SF', 'Sand Filtration'), ('DI', 'Disinfection'), ('OTHER', 'Other Treatment')], default='OTHER', max_length=100)),
                ('process_name', models.CharField(max_length=100)),
                ('num_units', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='scheme',
            name='treatment',
            field=models.ManyToManyField(blank=True, related_name='schemes', to='components.treatmentprocess'),
        ),
    ]
