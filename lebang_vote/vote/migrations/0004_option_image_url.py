# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20171219_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='image_url',
            field=models.CharField(blank=True, default=b'', max_length=1024),
        ),
    ]