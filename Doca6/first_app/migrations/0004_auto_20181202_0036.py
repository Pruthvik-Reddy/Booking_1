# Generated by Django 2.1.3 on 2018-12-01 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20181201_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 0, 36, 0, 311918)),
        ),
    ]
