# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0025_plantype_seqnumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaguecontent',
            options={'verbose_name': '\u6e20\u9053\u52a0\u76df-\u5185\u5bb9', 'verbose_name_plural': '\u6e20\u9053\u52a0\u76df-\u5185\u5bb9'},
        ),
        migrations.AddField(
            model_name='casetype',
            name='SeqNumber',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', blank=True),
        ),
        migrations.AddField(
            model_name='leaguecontent',
            name='SeqNumber',
            field=models.IntegerField(null=True, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', blank=True),
        ),
    ]
