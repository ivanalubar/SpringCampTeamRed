# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_auto_20170510_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_people',
            field=models.IntegerField(),
        ),
    ]
