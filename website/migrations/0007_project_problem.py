# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-19 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_barrier_benefit_collaborator_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
