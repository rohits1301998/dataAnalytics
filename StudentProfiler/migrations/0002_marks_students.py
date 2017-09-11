# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 11:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfiler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('ut1', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('ut2', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('sem', models.IntegerField(validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)])),
                ('total', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
    ]
