# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0023_auto_20170303_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='SeqNumber',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', blank=True),
        ),
    ]
