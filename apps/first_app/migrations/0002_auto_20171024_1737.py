# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='item_name',
        ),
        migrations.AddField(
            model_name='items',
            name='wishes',
            field=models.ManyToManyField(related_name='customers', to='first_app.users'),
        ),
    ]
