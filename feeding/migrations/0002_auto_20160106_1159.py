# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='wtDelta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
