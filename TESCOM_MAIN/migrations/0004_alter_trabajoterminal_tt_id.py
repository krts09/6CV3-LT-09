# Generated by Django 5.0.4 on 2024-06-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TESCOM_MAIN', '0003_remove_alumnotrabajoterminal_archivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajoterminal',
            name='tt_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
