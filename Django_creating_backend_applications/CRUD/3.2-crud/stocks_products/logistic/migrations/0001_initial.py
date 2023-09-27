# Generated by Django 4.2.4 on 2023-09-27 17:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18, validators=[django.core.validators.MinValueValidator(0)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.product')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='products',
            field=models.ManyToManyField(related_name='stocks', through='logistic.StockProduct', to='logistic.product'),
        ),
    ]
