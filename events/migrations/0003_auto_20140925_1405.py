# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='map_lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='map_lon',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
