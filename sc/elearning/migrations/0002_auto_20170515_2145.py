# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='data',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
