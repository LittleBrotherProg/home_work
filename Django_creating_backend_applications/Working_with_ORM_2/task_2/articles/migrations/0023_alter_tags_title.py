# Generated by Django 4.2.4 on 2023-09-21 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_tag_alter_tags_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Тег'),
        ),
    ]
