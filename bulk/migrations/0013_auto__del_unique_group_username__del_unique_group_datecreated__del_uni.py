# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Contact', fields ['dateupdated']
        db.delete_unique('bulk_contact', ['dateupdated'])

        # Removing unique constraint on 'Contact', fields ['contactnumber']
        db.delete_unique('bulk_contact', ['contactnumber'])

        # Removing unique constraint on 'Contact', fields ['groupname']
        db.delete_unique('bulk_contact', ['groupname'])

        # Removing unique constraint on 'Contact', fields ['datecreated']
        db.delete_unique('bulk_contact', ['datecreated'])

        # Removing unique constraint on 'Contact', fields ['username']
        db.delete_unique('bulk_contact', ['username'])

        # Removing unique constraint on 'Group', fields ['dateupdated']
        db.delete_unique('bulk_group', ['dateupdated'])

        # Removing unique constraint on 'Group', fields ['contact']
        db.delete_unique('bulk_group', ['contact_id'])

        # Removing unique constraint on 'Group', fields ['groupname']
        db.delete_unique('bulk_group', ['groupname'])

        # Removing unique constraint on 'Group', fields ['datecreated']
        db.delete_unique('bulk_group', ['datecreated'])

        # Removing unique constraint on 'Group', fields ['username']
        db.delete_unique('bulk_group', ['username'])


    def backwards(self, orm):
        # Adding unique constraint on 'Group', fields ['username']
        db.create_unique('bulk_group', ['username'])

        # Adding unique constraint on 'Group', fields ['datecreated']
        db.create_unique('bulk_group', ['datecreated'])

        # Adding unique constraint on 'Group', fields ['groupname']
        db.create_unique('bulk_group', ['groupname'])

        # Adding unique constraint on 'Group', fields ['contact']
        db.create_unique('bulk_group', ['contact_id'])

        # Adding unique constraint on 'Group', fields ['dateupdated']
        db.create_unique('bulk_group', ['dateupdated'])

        # Adding unique constraint on 'Contact', fields ['username']
        db.create_unique('bulk_contact', ['username'])

        # Adding unique constraint on 'Contact', fields ['datecreated']
        db.create_unique('bulk_contact', ['datecreated'])

        # Adding unique constraint on 'Contact', fields ['groupname']
        db.create_unique('bulk_contact', ['groupname'])

        # Adding unique constraint on 'Contact', fields ['contactnumber']
        db.create_unique('bulk_contact', ['contactnumber'])

        # Adding unique constraint on 'Contact', fields ['dateupdated']
        db.create_unique('bulk_contact', ['dateupdated'])


    models = {
        'bulk.contact': {
            'Meta': {'object_name': 'Contact'},
            'contactnumber': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'to': "orm['bulk.Group']"}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.customer': {
            'Meta': {'object_name': 'Customer'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'companyname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postalAddress': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.group': {
            'Meta': {'object_name': 'Group'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'groups'", 'null': 'True', 'to': "orm['bulk.Contact']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'groups'", 'null': 'True', 'to': "orm['bulk.Customer']"}),
            'datecreated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groupname': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'bulk.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'messages'", 'null': 'True', 'to': "orm['bulk.Customer']"}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bulk.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'scheduledate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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