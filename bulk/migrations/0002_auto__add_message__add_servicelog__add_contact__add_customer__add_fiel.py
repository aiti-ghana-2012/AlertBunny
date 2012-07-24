# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Adding model 'Contact'
        db.create_table('bulk_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['bulk.Customer'])),
        ))
        db.send_create_signal('bulk', ['Contact'])

        # Adding model 'Customer'
        db.create_table('bulk_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dateofbirth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('companyname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('postalAddress', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bulk', ['Customer'])

        # Adding field 'Person.fistname'
        db.add_column('bulk_person', 'fistname',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 7, 23, 0, 0), max_length=30),
                      keep_default=False)

        # Adding field 'Person.lastname'
        db.add_column('bulk_person', 'lastname',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 7, 23, 0, 0), max_length=30),
                      keep_default=False)

        # Adding field 'Person.email'
        db.add_column('bulk_person', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=2, unique=True, max_length=254),
                      keep_default=False)

        # Adding field 'Person.mobilenumber'
        db.add_column('bulk_person', 'mobilenumber',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('bulk_message')

        # Deleting model 'Servicelog'
        db.delete_table('bulk_servicelog')

        # Deleting model 'Contact'
        db.delete_table('bulk_contact')

        # Deleting model 'Customer'
        db.delete_table('bulk_customer')

        # Deleting field 'Person.fistname'
        db.delete_column('bulk_person', 'fistname')

        # Deleting field 'Person.lastname'
        db.delete_column('bulk_person', 'lastname')

        # Deleting field 'Person.email'
        db.delete_column('bulk_person', 'email')

        # Deleting field 'Person.mobilenumber'
        db.delete_column('bulk_person', 'mobilenumber')


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
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postalAddress': ('django.db.models.fields.TextField', [], {})
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
        'bulk.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'fistname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mobilenumber': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        },
        'bulk.servicelog': {
            'Meta': {'object_name': 'Servicelog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'smsstatus': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bulk']