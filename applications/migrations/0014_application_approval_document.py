# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-16 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_auto_20200114_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approval_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_approval_document', to='applications.Record'),
        ),
    ]
