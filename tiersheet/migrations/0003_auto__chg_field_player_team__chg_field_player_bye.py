# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.team'
        db.alter_column(u'tiersheet_player', 'team', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Player.bye'
        db.alter_column(u'tiersheet_player', 'bye', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Player.team'
        db.alter_column(u'tiersheet_player', 'team', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'Player.bye'
        db.alter_column(u'tiersheet_player', 'bye', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'tiersheet.player': {
            'Meta': {'ordering': "['order']", 'object_name': 'Player'},
            'bye': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['tiersheet']