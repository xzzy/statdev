# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('approvals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Approvals',
            new_name='Approval',
        ),
    ]