# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0019_productcontent2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcontent2',
            name='TypeID',
        ),
        migrations.DeleteModel(
            name='ProductContent2',
        ),
    ]
