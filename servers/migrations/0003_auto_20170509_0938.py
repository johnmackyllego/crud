# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-09 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20170509_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='mobile',
            field=models.CharField(default='', max_length=14),
        ),
    ]
