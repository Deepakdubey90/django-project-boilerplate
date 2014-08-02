# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'profiles_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile_user', to=orm['clients.Client'])),
            ('picture', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'profiles', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'profiles_userprofile')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'profile_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_user'", 'to': u"orm['clients.Client']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']