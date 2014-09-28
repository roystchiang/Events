# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20140925_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='events',
            name='end_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
