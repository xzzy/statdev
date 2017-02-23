# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20170223_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('vessel_type', models.SmallIntegerField(choices=[(0, 'Vessel'), (1, 'Craft')])),
                ('name', models.CharField(max_length=256)),
                ('vessel_id', models.CharField(max_length=256)),
                ('size', models.IntegerField()),
                ('engine', models.IntegerField()),
                ('passenger_capacity', models.IntegerField()),
                ('registration', models.ManyToManyField(to='applications.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='application',
            name='vessels',
            field=models.ManyToManyField(to='applications.Vessel'),
        ),
    ]
