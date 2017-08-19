# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 12:45
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import lego.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_user_internal_email_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='internal_email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='email.EmailAddress'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_username',
            field=models.CharField(error_messages={'unique': 'A user has already verified that student username.'}, help_text='30 characters or fewer. Letters, digits and ./-/_ only.', max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[a-z0-9-._]+$', 'Enter a valid username.  This value may contain only letters, numbers and ./-/_ characters.', 'invalid'), lego.utils.validators.ReservedNameValidator()]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.  This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid'), lego.utils.validators.ReservedNameValidator()]),
        ),
    ]