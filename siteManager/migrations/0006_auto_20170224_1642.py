# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0005_recruitcontent_isfinish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitcontent',
            name='Connection',
        ),
        migrations.RemoveField(
            model_name='recruitcontent',
            name='Otherthing',
        ),
        migrations.RemoveField(
            model_name='recruitcontent',
            name='Requirement',
        ),
        migrations.RemoveField(
            model_name='recruitcontent',
            name='Responsibility',
        ),
        migrations.RemoveField(
            model_name='recruitcontent',
            name='Worklocation',
        ),
        migrations.AddField(
            model_name='recruitcontent',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe6\x8b\x9b\xe8\x81\x98\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='recruitcontent',
            name='Attachment',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
    ]
