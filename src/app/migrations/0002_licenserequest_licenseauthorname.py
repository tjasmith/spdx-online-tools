# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-25 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenserequest',
            name='licenseAuthorName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
