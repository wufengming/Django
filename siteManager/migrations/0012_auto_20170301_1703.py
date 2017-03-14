# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0011_auto_20170301_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='AttachmentName',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='OrderNumber',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='CreateTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='ModifyTime',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
