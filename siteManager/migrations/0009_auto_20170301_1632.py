# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0008_auto_20170228_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='AttachmentName',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='AttachmentUrl',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='Type',
        ),
        migrations.AddField(
            model_name='attachment',
            name='Attachment',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6', blank=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='ForeiginID',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x96\x87\xe7\xab\xa0ID', to='siteManager.ProductContent'),
        ),
    ]
