# Generated by Django 5.0.4 on 2024-06-29 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TESCOM_MAIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoTrabajoTerminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='trabajos_terminales/')),
                ('alumno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TESCOM_MAIN.alumno')),
                ('trabajo_terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TESCOM_MAIN.trabajoterminal')),
            ],
            options={
                'unique_together': {('alumno_id', 'trabajo_terminal')},
            },
        ),
        migrations.DeleteModel(
            name='Alumno_Trabajo_Terminal',
        ),
    ]
