# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.username'
        db.add_column('bulk_message', 'username',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


        # Changing field 'Message.customer'
        db.alter_column('bulk_message', 'customer_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bulk.Customer']))

    def backwards(self, orm):
        # Deleting field 'Message.username'
        db.delete_column('bulk_message', 'username')


        # Changing field 'Message.customer'
        db.alter_column('bulk_message', 'customer_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bulk.Customer']))

    models = {
        'bulk.contact': {
            'Meta': {'object_name': 'Contact'},
            'contactnumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'contacts'", 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'to': "orm['bulk.Group']"}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.customer': {
            'Meta': {'object_name': 'Customer'},
            'companyname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postalAddress': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.group': {
            'Meta': {'object_name': 'Group'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'groups'", 'null': 'True', 'to': "orm['bulk.Contact']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'groups'", 'null': 'True', 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messages'", 'to': "orm['bulk.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'scheduledate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 31, 0, 0)'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.servicelog': {
            'Meta': {'object_name': 'Servicelog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smsstatus': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bulk']