# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160618_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=15),
        ),
    ]