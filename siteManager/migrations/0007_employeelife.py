# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0006_auto_20170224_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLife',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=100, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xaf\xb4\xe6\x98\x8e')),
                ('Attachment', models.FileField(upload_to=b'', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8a\xe4\xbc\xa0', blank=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e\xe6\x97\xb6\xe9\x97\xb4')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5458\u5de5\u751f\u6d3b',
                'verbose_name_plural': '\u5458\u5de5\u751f\u6d3b',
            },
        ),
    ]
