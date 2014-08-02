# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Posts'
        db.create_table(u'posts_posts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length='500')),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Client'])),
        ))
        db.send_create_signal(u'posts', ['Posts'])


    def backwards(self, orm):
        # Deleting model 'Posts'
        db.delete_table(u'posts_posts')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'posts.posts': {
            'Meta': {'object_name': 'Posts'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': "'500'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Client']"})
        }
    }

    complete_apps = ['posts']