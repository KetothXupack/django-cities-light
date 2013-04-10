# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('django_geonames_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('name_ascii', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None)),
            ('code2', self.gf('django.db.models.fields.CharField')(max_length=2, unique=True, null=True, blank=True)),
            ('code3', self.gf('django.db.models.fields.CharField')(max_length=3, unique=True, null=True, blank=True)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=2, db_index=True)),
            ('tld', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=5, blank=True)),
            ('geoname_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('django_geonames', ['Country'])

        # Adding model 'City'
        db.create_table('django_geonames_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('name_ascii', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None)),
            ('geoname_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geonames.Country'])),
        ))
        db.send_create_signal('django_geonames', ['City'])

        # Adding unique constraint on 'City', fields ['country', 'name']
        db.create_unique('django_geonames_city', ['country_id', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'City', fields ['country', 'name']
        db.delete_unique('django_geonames_city', ['country_id', 'name'])

        # Deleting model 'Country'
        db.delete_table('django_geonames_country')

        # Deleting model 'City'
        db.delete_table('django_geonames_city')


    models = {
        'django_geonames.city': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('country', 'name'),)", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['django_geonames.Country']"}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'django_geonames.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['django_geonames']
