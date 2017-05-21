# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0010_auto_20161129_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='profilepic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to=b'')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=900)),
                ('students', models.ManyToManyField(related_name='studentof', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]