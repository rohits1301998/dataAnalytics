# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentProfiler', '0002_marks_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='UID',
            field=models.CharField(max_length=14),
        ),
    ]