# Generated by Django 4.2.4 on 2023-09-21 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_tags_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles_tags',
            name='test',
        ),
    ]