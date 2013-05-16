# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.phone_code'
        db.add_column(u'django_geonames_country', 'phone_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.phone_enabled'
        db.add_column(u'django_geonames_country', 'phone_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.phone_code'
        db.delete_column(u'django_geonames_country', 'phone_code')

        # Deleting field 'Country.phone_enabled'
        db.delete_column(u'django_geonames_country', 'phone_enabled')


    models = {
        u'django_geonames.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geonames.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'preferred_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'reg_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geonames.Region']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'update_preferred_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'django_geonames.country': {
            'Meta': {'object_name': 'Country'},
            'code2': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'currency_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'}),
            'currency_name': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'phone_code': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'phone_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'preferred_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'reg_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'tld': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '5', 'blank': 'True'}),
            'update_preferred_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'django_geonames.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geonames.Country']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'geoname_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'name_ascii': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'preferred_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'}),
            'reg_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name_ascii'"}),
            'update_preferred_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['django_geonames']