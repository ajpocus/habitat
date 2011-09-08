# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BordersMI'
        db.create_table('borders_bordersmi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('statefp10', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('countyfp10', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cousubfp10', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cousubns10', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('geoid10', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name10', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('namelsad10', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lsad10', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('classfp10', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc10', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cnectafp10', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('nectafp10', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('nctadvfp10', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat10', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aland10', self.gf('django.db.models.fields.FloatField')()),
            ('awater10', self.gf('django.db.models.fields.FloatField')()),
            ('intptlat10', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('intptlon10', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=4269)),
        ))
        db.send_create_signal('borders', ['BordersMI'])


    def backwards(self, orm):
        
        # Deleting model 'BordersMI'
        db.delete_table('borders_bordersmi')


    models = {
        'borders.bordersmi': {
            'Meta': {'object_name': 'BordersMI'},
            'aland10': ('django.db.models.fields.FloatField', [], {}),
            'awater10': ('django.db.models.fields.FloatField', [], {}),
            'classfp10': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cnectafp10': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'countyfp10': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'cousubfp10': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cousubns10': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'funcstat10': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geoid10': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '4269'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat10': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'intptlon10': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'lsad10': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mtfcc10': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name10': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'namelsad10': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nctadvfp10': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'nectafp10': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'statefp10': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['borders']
