# Generated by Django 2.2.4 on 2019-09-14 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adopcion', '0002_auto_20190913_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=10)),
                ('Edad_aproximada', models.IntegerField()),
                ('Fecha_rescate', models.DateField()),
                ('Persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Adopcion.Persona')),
                ('Vacuna', models.ManyToManyField(blank=True, to='Mascota.Vacuna')),
            ],
        ),
    ]
