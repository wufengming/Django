# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0004_auto_20170224_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitcontent',
            name='IsFinish',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x8b\x9b\xe8\x81\x98\xe7\xbb\x93\xe6\x9d\x9f'),
        ),
    ]
