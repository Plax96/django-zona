# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buffete', '0002_auto_20171105_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='abogado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buffete.Abogado'),
        ),
    ]
