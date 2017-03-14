# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0012_auto_20170301_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='AttachmentName',
        ),
    ]
