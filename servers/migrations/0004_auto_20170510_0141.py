# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-10 01:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_auto_20170509_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
