# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 02:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailuser',
            name='organisation',
        ),
        migrations.AlterField(
            model_name='address',
            name='oscar_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_addresses', to='address.UserAddress'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profile_adresses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='fax_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Given name(s)'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='residential_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.Address'),
        ),
        migrations.AlterField(
            model_name='emailuser',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([]),
        ),
    ]
