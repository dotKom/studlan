# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-21 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0012_auto_20190721_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lan',
            name='map_link',
            field=models.CharField(blank=True, help_text=b'URL for an embedded map', max_length=300, verbose_name=b'map link'),
        ),
    ]