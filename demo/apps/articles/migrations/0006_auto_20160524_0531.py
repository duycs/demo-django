# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
    ]
