# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-17 06:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160629_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
