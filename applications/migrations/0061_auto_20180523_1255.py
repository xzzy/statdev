# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-23 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0060_conditionpredefined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionpredefined',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
    ]
