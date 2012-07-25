# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Group.datecreated'
        db.alter_column('bulk_group', 'datecreated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Group.dateupdated'
        db.alter_column('bulk_group', 'dateupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))
        # Adding field 'Contact.datecreated'
        db.add_column('bulk_contact', 'datecreated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 7, 25, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Contact.dateupdated'
        db.add_column('bulk_contact', 'dateupdated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 7, 25, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Customer.datecreated'
        db.add_column('bulk_customer', 'datecreated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 7, 25, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Customer.dateupdated'
        db.add_column('bulk_customer', 'dateupdated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 7, 25, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'Customer.dateofbirth'
        db.alter_column('bulk_customer', 'dateofbirth', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Group.datecreated'
        db.alter_column('bulk_group', 'datecreated', self.gf('django.db.models.fields.DateField')(auto_now=True))

        # Changing field 'Group.dateupdated'
        db.alter_column('bulk_group', 'dateupdated', self.gf('django.db.models.fields.DateField')(auto_now=True))
        # Deleting field 'Contact.datecreated'
        db.delete_column('bulk_contact', 'datecreated')

        # Deleting field 'Contact.dateupdated'
        db.delete_column('bulk_contact', 'dateupdated')

        # Deleting field 'Customer.datecreated'
        db.delete_column('bulk_customer', 'datecreated')

        # Deleting field 'Customer.dateupdated'
        db.delete_column('bulk_customer', 'dateupdated')


        # Changing field 'Customer.dateofbirth'
        db.alter_column('bulk_customer', 'dateofbirth', self.gf('django.db.models.fields.DateField')())

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
            'dateofbirth': ('django.db.models.fields.DateTimeField', [], {}),
            'dateupdated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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