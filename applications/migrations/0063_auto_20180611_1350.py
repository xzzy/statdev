# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-11 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0062_auto_20180605_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationcontact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]