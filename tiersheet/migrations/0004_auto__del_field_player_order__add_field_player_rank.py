# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.order'
        db.delete_column(u'tiersheet_player', 'order')

        # Adding field 'Player.rank'
        db.add_column(u'tiersheet_player', 'rank',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Player.order'
        db.add_column(u'tiersheet_player', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Player.rank'
        db.delete_column(u'tiersheet_player', 'rank')


    models = {
        u'tiersheet.fantasyprorank': {
            'Meta': {'object_name': 'FantasyProRank'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'tiersheet.player': {
            'Meta': {'ordering': "['rank']", 'object_name': 'Player'},
            'bye': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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