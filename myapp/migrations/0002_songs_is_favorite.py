# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
