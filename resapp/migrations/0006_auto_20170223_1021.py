# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-23 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resapp', '0005_auto_20170223_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resapp.RestaurantModel'),
        ),
    ]