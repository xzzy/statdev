# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 06:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0039_auto_20170522_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='document_pre_draft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_predraft', to='applications.Document'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 22, 14, 51, 30, 176166), verbose_name='Date'),
        ),
    ]
