# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-02 13:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drone_app', '0005_auto_20170202_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dronedata',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 2, 13, 54, 54, 661097, tzinfo=utc), editable=False, verbose_name='auto_now_add=true'),
        ),
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 2, 13, 54, 54, 658894, tzinfo=utc), editable=False, verbose_name='auto_now_add=true'),
        ),
    ]
