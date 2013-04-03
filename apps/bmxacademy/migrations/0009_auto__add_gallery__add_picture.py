# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('bmxacademy_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('bmxacademy', ['Gallery'])

        # Adding model 'Picture'
        db.create_table('bmxacademy_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bmxacademy.Gallery'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img_crop', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('bmxacademy', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('bmxacademy_gallery')

        # Deleting model 'Picture'
        db.delete_table('bmxacademy_picture')


    models = {
        'bmxacademy.email': {
            'Meta': {'object_name': 'Email'},
            'default_sender': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bmxacademy.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'bmxacademy.message': {
            'Meta': {'object_name': 'Message'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'bmxacademy.new': {
            'Meta': {'object_name': 'New'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_crop': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'bmxacademy.participant': {
            'Meta': {'object_name': 'Participant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'birth_number': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'camp_variant': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'cap_size': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '64'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'transfer': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'tshirt_size': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'bmxacademy.picture': {
            'Meta': {'object_name': 'Picture'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bmxacademy.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_crop': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'bmxacademy.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_code': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['bmxacademy']