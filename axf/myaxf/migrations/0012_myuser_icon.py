# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0011_minebtns1'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons', verbose_name='邮箱号'),
        ),
    ]