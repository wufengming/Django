# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0021_auto_20170302_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='SeqNumber',
            field=models.IntegerField(default=1, unique=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7'),
        ),
    ]
