# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0014_remove_myuser_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]
