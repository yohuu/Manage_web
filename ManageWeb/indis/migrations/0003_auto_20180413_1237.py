# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indis', '0002_auto_20180412_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11, default='18840847649'),
        ),
        migrations.AddField(
            model_name='student',
            name='psw',
            field=models.CharField(max_length=50, default='123456'),
        ),
        migrations.AddField(
            model_name='student',
            name='real_name',
            field=models.CharField(max_length=50, default='郑鹏威'),
        ),
    ]
