# Generated by Django 4.2.4 on 2023-09-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_tags_article_alter_tags_is_main_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='title',
            field=models.CharField(default=1, max_length=256, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
