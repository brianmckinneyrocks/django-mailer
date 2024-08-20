# -*- coding: utf-8 -*-
import base64
import pickle
import datetime
from south.db import db
from south.v2 import DataMigration
from django.core.mail.message import EmailMessage
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for message in orm.Message.objects.all():
            core_msg = EmailMessage(
                 subject=message.subject,
                 body=message.message_body,
                 from_email=message.from_address,
                 to=[message.to_address],
            )
            core_msg_encoded = base64.encodestring(pickle.dumps(core_msg))
            message.message_data = core_msg_encoded
            message.save()

        for message in orm.MessageLog.objects.all():
            core_msg = EmailMessage(
                 subject=message.subject,
                 body=message.message_body,
                 from_email=message.from_address,
                 to=[message.to_address],
            )
            core_msg_encoded = base64.encodestring(pickle.dumps(core_msg))
            message.message_data = core_msg_encoded
            message.save() 

    def backwards(self, orm):
        "Remove messge_data data."
        for message in orm.Message.objects.all():
            message.message_data = ''
            message.save() 
  
        for message in orm.MessageLog.objects.all():
            message.message_data = ''
            message.save() 

    models = {
        u'mailer.dontsendentry': {
            'Meta': {'object_name': 'DontSendEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'mailer.message': {
            'Meta': {'object_name': 'Message'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_body': ('django.db.models.fields.TextField', [], {}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '1'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'mailer.messagelog': {
            'Meta': {'object_name': 'MessageLog'},
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_message': ('django.db.models.fields.TextField', [], {}),
            'message_body': ('django.db.models.fields.TextField', [], {}),
            'message_data': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'when_attempted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['mailer']
    symmetrical = True
