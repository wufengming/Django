# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0013_remove_attachment_attachmentname'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OrderNumber', models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\x8f\xb7')),
                ('Attachment', models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('ForeiginID', models.ForeignKey(verbose_name=b'\xe6\x96\xb9\xe6\xa1\x88\xe5\x86\x85\xe5\xae\xb9', to='siteManager.PlanContent')),
            ],
            options={
                'verbose_name': '\u65b9\u6848\u5185\u5bb9-\u9644\u4ef6',
                'verbose_name_plural': '\u65b9\u6848\u5185\u5bb9-\u9644\u4ef6',
            },
        ),
    ]
