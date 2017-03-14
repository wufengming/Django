# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0024_auto_20170303_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantype',
            name='SeqNumber',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', blank=True),
        ),
    ]
