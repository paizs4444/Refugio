# Generated by Django 2.2.5 on 2019-09-16 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adopcion', '0008_auto_20190915_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='Telefono',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
