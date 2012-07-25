# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Customer.name'
        db.delete_column('bulk_customer', 'name')

        # Adding field 'Customer.firstname'
        db.add_column('bulk_customer', 'firstname',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=30),
                      keep_default=False)

        # Adding field 'Customer.lastname'
        db.add_column('bulk_customer', 'lastname',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Customer.name'
        db.add_column('bulk_customer', 'name',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=30),
                      keep_default=False)

        # Deleting field 'Customer.firstname'
        db.delete_column('bulk_customer', 'firstname')

        # Deleting field 'Customer.lastname'
        db.delete_column('bulk_customer', 'lastname')


    models = {
        'bulk.contact': {
            'Meta': {'object_name': 'Contact'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['bulk.Group']"}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.customer': {
            'Meta': {'object_name': 'Customer'},
            'companyname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'max_length': '15', 'blank': 'True'}),
            'postaladdress': ('django.db.models.fields.TextField', [], {})
        },
        'bulk.group': {
            'Meta': {'object_name': 'Group'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['bulk.Contact']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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