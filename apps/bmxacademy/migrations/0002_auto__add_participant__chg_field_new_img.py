# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participant'
        db.create_table('bmxacademy_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birth_number', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=64)),
            ('tshirt_size', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('cap_size', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('camp_variant', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('transfer', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('bmxacademy', ['Participant'])


        # Changing field 'New.img'
        db.alter_column('bmxacademy_new', 'img', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table('bmxacademy_participant')


        # Changing field 'New.img'
        db.alter_column('bmxacademy_new', 'img', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        'bmxacademy.new': {
            'Meta': {'object_name': 'New'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
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
            'transfer': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'tshirt_size': ('django.db.models.fields.CharField', [], {'max_length': '8'})
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