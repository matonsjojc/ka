# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ka', '0008_auto_20160613_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nastavitve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='odgovor',
            name='datum_objave',
            field=models.DateTimeField(null=True, verbose_name='datum objave'),
        ),
        migrations.AddField(
            model_name='odgovor',
            name='komentar_k_tekstu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='odgovor',
            name='tekst',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='odgovor',
            name='vprasanje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ka.Vprasanje'),
        ),
        migrations.AlterField(
            model_name='vprasanje',
            name='aktiven',
            field=models.BooleanField(default=True),
        ),
    ]
