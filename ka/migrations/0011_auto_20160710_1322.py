# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ka', '0010_auto_20160613_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odgovor',
            name='datum_objave',
        ),
        migrations.RemoveField(
            model_name='odgovor',
            name='komentar_k_tekstu',
        ),
        migrations.RemoveField(
            model_name='vprasanje',
            name='datum_objave',
        ),
        migrations.AlterField(
            model_name='vprasanje',
            name='komentar_k_tekstu',
            field=models.TextField(blank=True, null=True),
        ),
    ]
