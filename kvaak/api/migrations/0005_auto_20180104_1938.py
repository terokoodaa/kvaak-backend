# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180104_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='dateTime',
            field=models.DateTimeField(db_column='dateTime'),
        ),
    ]
