# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteManager', '0020_auto_20170302_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plancontent',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
    ]
