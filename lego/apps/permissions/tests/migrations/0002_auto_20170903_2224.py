# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='require_auth',
            field=models.BooleanField(default=True),
        ),
    ]