# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0007_employeelife'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casecontent',
            name='ProductType',
        ),
        migrations.AlterField(
            model_name='casecontent',
            name='Attachment',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='casecontent',
            name='Summary',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='casecontent',
            name='Title',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
