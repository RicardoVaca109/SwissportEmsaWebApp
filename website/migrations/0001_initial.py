# Generated by Django 5.1.4 on 2025-01-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(choices=[('Administrador', 'Administrador'), ('KAM', 'KAM'), ('Supervisor', 'Supervisor')], max_length=50)),
            ],
        ),
    ]
