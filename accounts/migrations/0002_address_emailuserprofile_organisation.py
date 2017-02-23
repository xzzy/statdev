# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 05:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=255, verbose_name='Line 1')),
                ('line2', models.CharField(blank=True, max_length=255, verbose_name='Line 2')),
                ('locality', models.CharField(max_length=255, verbose_name='Suburb / Town')),
                ('state', models.CharField(blank=True, choices=[(1, 'ACT'), (2, 'NSW'), (3, 'NT'), (4, 'QLD'), (5, 'SA'), (6, 'TAS'), (7, 'VIC'), (8, 'WA')], default=8, max_length=255, null=True)),
                ('postcode', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='EmailUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(null=True, verbose_name='date of birth')),
                ('identification', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('id_verified', models.DateField(null=True, verbose_name='ID verified')),
                ('home_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_billing_address', to='accounts.Address')),
                ('emailuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postal_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_postal_address', to='accounts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('abn', models.CharField(blank=True, max_length=50, null=True)),
                ('identification', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_billing_address', to='accounts.Address')),
                ('delegates', models.ManyToManyField(blank=True, to='accounts.EmailUserProfile')),
                ('postal_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_postal_address', to='accounts.Address')),
            ],
        ),
    ]
