# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20150803_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='orderDueDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 15, 8, 3, 12, 522863, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
