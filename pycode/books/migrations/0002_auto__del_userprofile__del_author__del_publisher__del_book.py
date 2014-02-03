# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'books_userprofile')

        # Deleting model 'Author'
        db.delete_table(u'books_author')

        # Deleting model 'Publisher'
        db.delete_table(u'books_publisher')

        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'books_book_authors'))


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'books_userprofile', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'books', ['UserProfile'])

        # Adding model 'Author'
        db.create_table(u'books_author', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'books', ['Author'])

        # Adding model 'Publisher'
        db.create_table(u'books_publisher', (
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'books', ['Publisher'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['books.Publisher'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])


    models = {
        
    }

    complete_apps = ['books']