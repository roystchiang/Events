# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20140926_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'events', blank=True),
            preserve_default=True,
        ),
    ]
