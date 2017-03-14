# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0017_auto_20170302_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontent',
            name='ProductType',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbb\x86\xe7\xb1\xbb', blank=True),
        ),
    ]
