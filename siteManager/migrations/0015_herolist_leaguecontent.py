# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0014_attachmentplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(default='\u6e20\u9053', max_length=10, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab')),
                ('Name', models.CharField(max_length=100, verbose_name=b'\xe8\x8b\xb1\xe9\x9b\x84\xe5\x90\x8d\xe7\xa7\xb0')),
                ('SeqNumber', models.IntegerField(default=1, unique=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7')),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u82f1\u96c4\u699c',
                'verbose_name_plural': '\u82f1\u96c4\u699c',
            },
        ),
        migrations.CreateModel(
            name='LeagueContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ContentType', models.CharField(default='\u7533\u8bf7\u52a0\u76df', max_length=10, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe7\xb1\xbb\xe5\x88\xab', choices=[('\u7533\u8bf7\u52a0\u76df', '\u7533\u8bf7\u52a0\u76df'), ('\u652f\u6301\u4fdd\u969c', '\u652f\u6301\u4fdd\u969c'), ('\u4f19\u4f34\u4f53\u7cfb', '\u4f19\u4f34\u4f53\u7cfb'), ('\u4f19\u4f34\u62db\u8058', '\u4f19\u4f34\u62db\u8058')])),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9')),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u52a0\u76df\u6211\u4eec\u5185\u5bb9',
                'verbose_name_plural': '\u52a0\u76df\u6211\u4eec\u5185\u5bb9',
            },
        ),
    ]
