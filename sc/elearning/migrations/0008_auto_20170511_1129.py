# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_auto_20170511_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.Groups'),
        ),
        migrations.AlterField(
            model_name='course',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ind_provider_profile', to='elearning.Groups'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_created', to='elearning.Groups'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start',
            field=models.DateField(),
        ),
    ]
