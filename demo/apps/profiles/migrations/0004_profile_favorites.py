# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
        ('profiles', '0003_auto_20160521_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='articles.Article'),
        ),
    ]
