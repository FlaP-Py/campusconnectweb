# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160617_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sessionId',
        ),
        migrations.AddField(
            model_name='user',
            name='gprofileId',
            field=models.CharField(
                default=None, max_length=40, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='profileId',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
