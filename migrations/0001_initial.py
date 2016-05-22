# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 13:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.TextField()),
                ('cycle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('WE', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.TextField(default=1)),
                ('number_of_hours', models.TextField(default=120)),
            ],
        ),
    ]