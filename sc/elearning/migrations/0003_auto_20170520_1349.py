# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 11:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_course_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]