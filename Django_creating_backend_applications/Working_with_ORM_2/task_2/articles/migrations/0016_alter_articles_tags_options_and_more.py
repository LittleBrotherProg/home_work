# Generated by Django 4.2.4 on 2023-09-21 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_alter_articles_tags_options_tags_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles_tags',
            options={},
        ),
        migrations.RemoveField(
            model_name='articles_tags',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='is_main',
        ),
        migrations.AddField(
            model_name='articles_tags',
            name='is_main',
            field=models.BooleanField(default=1, verbose_name='Основной'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Категории'),
            preserve_default=False,
        ),
    ]
