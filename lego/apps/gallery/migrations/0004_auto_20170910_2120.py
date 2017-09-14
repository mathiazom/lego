# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 21:20
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0003_gallery_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypicture',
            name='taggees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_covers', to='gallery.GalleryPicture'),
        ),
    ]