# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5927\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5927\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductType', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Summary', models.CharField(max_length=200, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9')),
                ('Hits', models.IntegerField(default=0, null=True, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('PublishTime', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('IsHot', models.BooleanField(verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x83\xad\xe9\x97\xa8')),
                ('Attachment', models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('Editor', models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe8\x80\x85', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('Category', models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\xa4\xa7\xe7\xb1\xbb', to='siteManager.ArticleCategory')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5185\u5bb9',
                'verbose_name_plural': '\u6587\u7ae0\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u7c7b\u522b',
                'verbose_name_plural': '\u6587\u7ae0\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ForeiginID', models.IntegerField(verbose_name=b'\xe5\xa4\x96\xe9\x94\xae')),
                ('Type', models.CharField(max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab')),
                ('AttachmentName', models.CharField(max_length=100, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6\xe5\x90\x8d\xe7\xa7\xb0')),
                ('AttachmentUrl', models.CharField(max_length=200, verbose_name=b'\xe5\xad\x98\xe5\x82\xa8\xe8\xb7\xaf\xe5\xbe\x84')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\x9d\xe5\xad\x98\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u9644\u4ef6',
                'verbose_name_plural': '\u9644\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='CaseContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductType', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Summary', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9')),
                ('Hits', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0', null=True, editable=False, blank=True)),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('Attachment', models.CharField(max_length=200, null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u6848\u4f8b\u5185\u5bb9',
                'verbose_name_plural': '\u6848\u4f8b\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('EnglishName', models.CharField(max_length=100, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u6848\u4f8b\u7c7b\u522b',
                'verbose_name_plural': '\u6848\u4f8b\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='PlanContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductType', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Summary', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9')),
                ('Hits', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0', null=True, editable=False, blank=True)),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('Attachment', models.CharField(max_length=200, null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u65b9\u6848\u5185\u5bb9',
                'verbose_name_plural': '\u65b9\u6848\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='PlanType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('EnglishName', models.CharField(max_length=100, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u65b9\u6848\u7c7b\u522b',
                'verbose_name_plural': '\u65b9\u6848\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='ProductContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ProductType', models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('Summary', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9')),
                ('Hits', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0', null=True, editable=False, blank=True)),
                ('IsPublish', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83')),
                ('Attachment', models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u5185\u5bb9',
                'verbose_name_plural': '\u4ea7\u54c1\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('Name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('EnglishName', models.CharField(max_length=100, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7c7b\u522b',
                'verbose_name_plural': '\u4ea7\u54c1\u7c7b\u522b',
            },
        ),
        migrations.AddField(
            model_name='productcontent',
            name='TypeID',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.ProductType'),
        ),
        migrations.AddField(
            model_name='plancontent',
            name='TypeID',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\xb9\xe6\xa1\x88\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.PlanType'),
        ),
        migrations.AddField(
            model_name='casecontent',
            name='TypeID',
            field=models.ForeignKey(verbose_name=b'\xe6\xa1\x88\xe4\xbe\x8b\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.CaseType'),
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='Type',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\xb1\xbb\xe5\x88\xab', to='siteManager.ArticleType'),
        ),
    ]
