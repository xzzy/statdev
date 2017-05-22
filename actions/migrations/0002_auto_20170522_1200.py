# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Communicate'), (2, 'Assign'), (3, 'Refer'), (4, 'Issue'), (5, 'Decline'), (6, 'Publish'), (7, 'Lodge'), (8, 'Next Step')], null=True),
        ),
    ]
