# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.group'
        db.add_column('bulk_contact', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='contacts', to=orm['bulk.Group']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.group'
        db.delete_column('bulk_contact', 'group_id')


    models = {
        'bulk.contact': {
            'Meta': {'object_name': 'Contact'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['bulk.Customer']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['bulk.Group']"}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.customer': {
            'Meta': {'object_name': 'Customer'},
            'companyname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postalAddress': ('django.db.models.fields.TextField', [], {})
        },
        'bulk.group': {
            'Meta': {'object_name': 'Group'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['bulk.Contact']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.message': {
            'Meta': {'object_name': 'Message'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['bulk.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scheduledate': ('django.db.models.fields.DateField', [], {}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.servicelog': {
            'Meta': {'object_name': 'Servicelog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smsstatus': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bulk']