# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-20 14:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.TextField(validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
