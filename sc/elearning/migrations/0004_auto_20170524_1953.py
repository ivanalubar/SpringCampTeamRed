# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_auto_20170523_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(default=''),
        ),
    ]