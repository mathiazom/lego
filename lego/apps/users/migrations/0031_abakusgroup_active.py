# Generated by Django 3.0.14 on 2021-11-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0030_auto_20211018_2036"),
    ]

    operations = [
        migrations.AddField(
            model_name="abakusgroup",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
