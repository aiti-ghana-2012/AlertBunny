# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('bulk_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('mobilenumber', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dateupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dateofbirth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('companyname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('postalAddress', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bulk', ['Customer'])

        # Adding model 'Contact'
        db.create_table('bulk_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['bulk.Group'])),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dateupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['bulk.Customer'])),
        ))
        db.send_create_signal('bulk', ['Contact'])

        # Adding model 'Group'
        db.create_table('bulk_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('datecreated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dateupdated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['bulk.Customer'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['bulk.Contact'])),
        ))
        db.send_create_signal('bulk', ['Group'])

        # Adding model 'Message'
        db.create_table('bulk_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('receiver', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('scheduledate', self.gf('django.db.models.fields.DateField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messages', to=orm['bulk.Customer'])),
        ))
        db.send_create_signal('bulk', ['Message'])

        # Adding model 'Servicelog'
        db.create_table('bulk_servicelog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('smsstatus', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bulk', ['Servicelog'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('bulk_customer')

        # Deleting model 'Contact'
        db.delete_table('bulk_contact')

        # Deleting model 'Group'
        db.delete_table('bulk_group')

        # Deleting model 'Message'
        db.delete_table('bulk_message')

        # Deleting model 'Servicelog'
        db.delete_table('bulk_servicelog')


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
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
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