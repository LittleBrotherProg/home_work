# Generated by Django 4.2.4 on 2023-09-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='time',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
