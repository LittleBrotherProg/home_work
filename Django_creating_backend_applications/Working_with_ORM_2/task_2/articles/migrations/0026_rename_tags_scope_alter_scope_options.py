# Generated by Django 4.2.4 on 2023-09-21 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_tags_is_main'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Scope',
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={},
        ),
    ]
