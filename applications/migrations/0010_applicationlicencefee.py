# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-09-20 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_application_assigned_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLicenceFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type', models.IntegerField(blank=True, choices=[(1, 'Permit'), (2, 'Licence/permit'), (3, 'Part 5'), (4, 'Emergency works'), (5, 'Part 5 - Amendment Request'), (6, 'Part 5 - Amendment Application'), (7, 'Test - Application'), (8, 'Amend Permit'), (9, 'Amend Licence'), (10, 'Renew Permit'), (11, 'Renew Licence')], null=True)),
                ('licence_fee', models.DecimalField(decimal_places=2, default='0.00', max_digits=8)),
                ('start_dt', models.DateTimeField(blank=True, null=True)),
                ('end_dt', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
