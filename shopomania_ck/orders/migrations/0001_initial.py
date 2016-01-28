# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, unique=True, verbose_name='ФИО покупателя')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание товара')),
                ('price', models.PositiveIntegerField(verbose_name='Цена товара')),
                ('link', models.CharField(max_length=1024, verbose_name='Ссылка на сайт с описанием товара')),
                ('comment', models.CharField(max_length=200, null=True, verbose_name='Комментарий')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа')),
                ('description', models.CharField(max_length=150, null=True, verbose_name='Описание заказа')),
                ('author', models.CharField(max_length=50, null=True, verbose_name='Составитель')),
                ('comment', models.CharField(max_length=200, null=True, verbose_name='Комментарий')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
