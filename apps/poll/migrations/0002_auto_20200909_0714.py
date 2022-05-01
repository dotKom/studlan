# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-09 07:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollparticipant',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.PollOption', verbose_name='option'),
        ),
        migrations.AlterField(
            model_name='pollparticipant',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Poll', verbose_name='poll'),
        ),
        migrations.AlterField(
            model_name='pollparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]