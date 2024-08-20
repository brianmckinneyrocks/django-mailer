# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.message_body'
        db.delete_column(u'mailer_message', 'message_body')

        # Deleting field 'Message.to_address'
        db.delete_column(u'mailer_message', 'to_address')

        # Deleting field 'Message.from_address'
        db.delete_column(u'mailer_message', 'from_address')

        # Deleting field 'Message.subject'
        db.delete_column(u'mailer_message', 'subject')

        # Deleting field 'MessageLog.message_body'
        db.delete_column(u'mailer_messagelog', 'message_body')

        # Deleting field 'MessageLog.to_address'
        db.delete_column(u'mailer_messagelog', 'to_address')

        # Deleting field 'MessageLog.from_address'
        db.delete_column(u'mailer_messagelog', 'from_address')

        # Deleting field 'MessageLog.subject'
        db.delete_column(u'mailer_messagelog', 'subject')


    def backwards(self, orm):
        # Adding field 'Message.message_body'
        db.add_column(u'mailer_message', 'message_body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Message.to_address'
        db.add_column(u'mailer_message', 'to_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Message.from_address'
        db.add_column(u'mailer_message', 'from_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Message.subject'
        db.add_column(u'mailer_message', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'MessageLog.message_body'
        db.add_column(u'mailer_messagelog', 'message_body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'MessageLog.to_address'
        db.add_column(u'mailer_messagelog', 'to_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'MessageLog.from_address'
        db.add_column(u'mailer_messagelog', 'from_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'MessageLog.subject'
        db.add_column(u'mailer_messagelog', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    models = {
        u'mailer.dontsendentry': {
            'Meta': {'object_name': 'DontSendEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'mailer.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'mailer.messagelog': {
            'Meta': {'object_name': 'MessageLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_message': ('django.db.models.fields.TextField', [], {}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'when_attempted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['mailer']