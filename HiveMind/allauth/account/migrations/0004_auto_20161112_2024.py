# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
