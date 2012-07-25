# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('bulk_person')

        # Adding model 'Group'
        db.create_table('bulk_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('datecreated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('dateupdated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['bulk.Customer'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['bulk.Contact'])),
        ))
        db.send_create_signal('bulk', ['Group'])

        # Adding field 'Customer.fistname'
        db.add_column('bulk_customer', 'fistname',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Customer.lastname'
        db.add_column('bulk_customer', 'lastname',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=30),
                      keep_default=False)

        # Adding field 'Customer.email'
        db.add_column('bulk_customer', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, unique=True, max_length=254),
                      keep_default=False)

        # Adding field 'Customer.mobilenumber'
        db.add_column('bulk_customer', 'mobilenumber',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, unique=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Person'
        db.create_table('bulk_person', (
            ('mobilenumber', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True)),
            ('fistname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('bulk', ['Person'])

        # Deleting model 'Group'
        db.delete_table('bulk_group')

        # Deleting field 'Customer.fistname'
        db.delete_column('bulk_customer', 'fistname')

        # Deleting field 'Customer.lastname'
        db.delete_column('bulk_customer', 'lastname')

        # Deleting field 'Customer.email'
        db.delete_column('bulk_customer', 'email')

        # Deleting field 'Customer.mobilenumber'
        db.delete_column('bulk_customer', 'mobilenumber')


    models = {
        'bulk.contact': {
            'Meta': {'object_name': 'Contact'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['bulk.Customer']"}),
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bulk.customer': {
            'Meta': {'object_name': 'Customer'},
            'companyname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'fistname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
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