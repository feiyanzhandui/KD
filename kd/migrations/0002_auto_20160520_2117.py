# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='weight',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]