# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-25 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0039_auto_20171012_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='proposed_conditions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
