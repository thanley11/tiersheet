# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FantasyProRank'
        db.create_table(u'tiersheet_fantasyprorank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'tiersheet', ['FantasyProRank'])


    def backwards(self, orm):
        # Deleting model 'FantasyProRank'
        db.delete_table(u'tiersheet_fantasyprorank')


    models = {
        u'tiersheet.fantasyprorank': {
            'Meta': {'object_name': 'FantasyProRank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'tiersheet.player': {
            'Meta': {'ordering': "['order']", 'object_name': 'Player'},
            'bye': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'tiersheet.rotoworld_url': {
            'Meta': {'object_name': 'Rotoworld_Url'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'roto_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tiersheet']