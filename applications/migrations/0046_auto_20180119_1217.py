# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-19 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0045_auto_20180119_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compliancegroup',
            name='cid',
        ),
        migrations.AddField(
            model_name='compliance',
            name='compliance_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='applications.ComplianceGroup'),
        ),
    ]
