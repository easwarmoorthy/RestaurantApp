# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resapp', '0007_auto_20170223_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='restaurant',
            field=models.ManyToManyField(blank=True, null=True, to='resapp.RestaurantModel'),
        ),
    ]
