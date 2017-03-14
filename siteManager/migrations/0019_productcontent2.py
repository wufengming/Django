# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0018_auto_20170302_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductContent2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductType', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Summary', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('Hits', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0', null=True, editable=False, blank=True)),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('Attachment', models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('TypeID', models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.ProductType')),
            ],
        ),
    ]
