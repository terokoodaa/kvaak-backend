# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='date_time',
            new_name='dateTime',
        ),
    ]