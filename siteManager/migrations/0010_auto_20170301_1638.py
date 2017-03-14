# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0009_auto_20170301_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': '\u4ea7\u54c1\u5185\u5bb9-\u9644\u4ef6', 'verbose_name_plural': '\u4ea7\u54c1\u5185\u5bb9-\u9644\u4ef6'},
        ),
        migrations.AddField(
            model_name='attachment',
            name='OrderNumber',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\x8f\xb7'),
        ),
    ]
