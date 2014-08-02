# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserProfile.info'
        db.alter_column(u'profiles_userprofile', 'info', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'UserProfile.info'
        db.alter_column(u'profiles_userprofile', 'info', self.gf('django.db.models.fields.CharField')(max_length=150))

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
            'info': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'profile_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile_user'", 'to': u"orm['clients.Client']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']