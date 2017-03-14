# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0010_auto_20170301_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='OrderNumber',
        ),
        migrations.AlterField(
            model_name='attachment',
            name='ForeiginID',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x86\x85\xe5\xae\xb9', to='siteManager.ProductContent'),
        ),
    ]
