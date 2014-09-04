# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'Post title')),
                ('content', models.TextField(max_length=b'500', verbose_name=b'Post Content')),
                ('tags', models.CharField(max_length=90, null=True, verbose_name=b'tags', blank=True)),
                ('time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('user', models.ForeignKey(related_name=b'user', to='clients.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
