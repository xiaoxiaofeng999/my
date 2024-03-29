# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaxf', '0010_minebtns_is_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='MineBtnS1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btn', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=140)),
                ('bref_url', models.CharField(max_length=255, null=True)),
                ('is_used', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '我的页面的上一排按钮',
            },
        ),
    ]
