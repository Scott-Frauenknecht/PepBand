# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PepBandWebsite', '0019_eboard_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='video',
            field=models.CharField(default='', max_length=100),
        ),
    ]
