# Generated by Django 4.2.4 on 2023-09-20 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_tags_name_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='test1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Tag'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Articles_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ManyToManyField(related_name='XZ', to='articles.article')),
            ],
        ),
        migrations.AlterField(
            model_name='tags',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles_tags', verbose_name='Tag'),
        ),
    ]
