# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeding', '0008_auto_20160321_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='bathroom',
            field=models.CharField(blank=True, choices=[('urine', 'urine'), ('bm', 'bowel movement'), ('none', 'none')], max_length=12),
        ),
    ]
