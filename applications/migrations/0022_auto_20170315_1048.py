# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 02:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0021_auto_20170313_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='current_land_use',
        ),
        migrations.RemoveField(
            model_name='application',
            name='proposed_development_description',
        ),
        migrations.RemoveField(
            model_name='application',
            name='river_reserve_lease',
        ),
    ]
