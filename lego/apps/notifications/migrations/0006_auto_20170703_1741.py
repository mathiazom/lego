# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 17:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20170524_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsetting',
            name='channels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('email', 'email'), ('push', 'push')], max_length=64), default=['email', 'push'], null=True, size=None),
        ),
    ]