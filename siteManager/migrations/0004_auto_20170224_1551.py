# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0003_auto_20170220_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Position', models.CharField(max_length=50, verbose_name=b'\xe6\x8b\x9b\xe8\x81\x98\xe8\x81\x8c\xe4\xbd\x8d', blank=True)),
                ('Responsibility', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe5\xb2\x97\xe4\xbd\x8d\xe8\x81\x8c\xe8\xb4\xa3', blank=True)),
                ('Requirement', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe4\xbb\xbb\xe8\x81\x8c\xe8\xa6\x81\xe6\xb1\x82', blank=True)),
                ('Worklocation', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x9c\xb0\xe7\x82\xb9', blank=True)),
                ('Connection', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f', blank=True)),
                ('Otherthing', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True)),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('Attachment', models.CharField(max_length=200, null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u62db\u8058\u5185\u5bb9',
                'verbose_name_plural': '\u62db\u8058\u5185\u5bb9',
            },
        ),
        migrations.AddField(
            model_name='casecontent',
            name='Area',
            field=models.CharField(default='\u6d59\u6c5f', max_length=10, verbose_name=b'\xe5\x8c\xba\xe5\x9f\x9f', choices=[('\u5317\u4eac', '\u5317\u4eac'), ('\u5929\u6d25', '\u5929\u6d25'), ('\u4e0a\u6d77', '\u4e0a\u6d77'), ('\u91cd\u5e86', '\u91cd\u5e86'), ('\u6cb3\u5317', '\u6cb3\u5317'), ('\u6cb3\u5357', '\u6cb3\u5357'), ('\u4e91\u5357', '\u4e91\u5357'), ('\u8fbd\u5b81', '\u8fbd\u5b81'), ('\u9ed1\u9f99\u6c5f', '\u9ed1\u9f99\u6c5f'), ('\u6e56\u5357', '\u6e56\u5357'), ('\u5b89\u5fbd', '\u5b89\u5fbd'), ('\u5c71\u4e1c', '\u5c71\u4e1c'), ('\u65b0\u7586', '\u65b0\u7586'), ('\u6c5f\u82cf', '\u6c5f\u82cf'), ('\u6d59\u6c5f', '\u6d59\u6c5f'), ('\u6c5f\u897f', '\u6c5f\u897f'), ('\u6e56\u5317', '\u6e56\u5317'), ('\u5e7f\u897f', '\u5e7f\u897f'), ('\u5c71\u897f', '\u5c71\u897f'), ('\u5185\u8499\u53e4', '\u5185\u8499\u53e4'), ('\u9655\u897f', '\u9655\u897f'), ('\u5409\u6797', '\u5409\u6797'), ('\u798f\u5efa', '\u798f\u5efa'), ('\u8d35\u5dde', '\u8d35\u5dde'), ('\u5e7f\u4e1c', '\u5e7f\u4e1c'), ('\u9752\u6d77', '\u9752\u6d77'), ('\u897f\u85cf', '\u897f\u85cf'), ('\u56db\u5ddd', '\u56db\u5ddd'), ('\u5b81\u590f', '\u5b81\u590f'), ('\u6d77\u5357', '\u6d77\u5357'), ('\u53f0\u6e7e', '\u53f0\u6e7e'), ('\u9999\u6e2f', '\u9999\u6e2f'), ('\u6fb3\u95e8', '\u6fb3\u95e8'), ('\u5357\u6d77\u8bf8\u5c9b', '\u5357\u6d77\u8bf8\u5c9b')]),
        ),
        migrations.AlterField(
            model_name='casecontent',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='casecontent',
            name='TypeID',
            field=models.ForeignKey(related_name='TypeName', verbose_name=b'\xe6\xa1\x88\xe4\xbe\x8b\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.CaseType'),
        ),
    ]
