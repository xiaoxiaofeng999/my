# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0013_auto_20181106_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='icon',
        ),
    ]
