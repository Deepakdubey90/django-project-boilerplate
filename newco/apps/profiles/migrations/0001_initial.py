# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.FileField(upload_to=b'media/%Y/%m/%d')),
                ('info', models.TextField(max_length=500, verbose_name=b'Profile Information')),
                ('status', models.CharField(max_length=100, verbose_name=b'status')),
                ('profile_user', models.ForeignKey(related_name=b'profile_user', verbose_name=b'Profile User', to='clients.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
