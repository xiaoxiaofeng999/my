# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0008_auto_20181105_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='MineBtnS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btn', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=140)),
                ('bref_url', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': '我的页面的下一排按钮',
            },
        ),
    ]
