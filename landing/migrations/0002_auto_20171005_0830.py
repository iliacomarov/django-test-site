# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscraber_email',
            new_name='subscriber_email',
        ),
    ]
