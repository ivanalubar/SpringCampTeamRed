# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 10:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0012_auto_20170511_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='users',
        ),
    ]