# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Username')),
                ('email', models.EmailField(max_length=150, verbose_name=b'Email')),
                ('address', models.TextField(max_length=200, verbose_name=b'Address')),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'clients',
            },
            bases=(models.Model,),
        ),
    ]
