# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_auto_20170516_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
