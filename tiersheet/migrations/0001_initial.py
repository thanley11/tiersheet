# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'tiersheet_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bye', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('team', self.gf('django.db.models.fields.CharField')(default=None, max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal(u'tiersheet', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'tiersheet_player')


    models = {
        u'tiersheet.player': {
            'Meta': {'ordering': "['order']", 'object_name': 'Player'},
            'bye': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tiersheet']