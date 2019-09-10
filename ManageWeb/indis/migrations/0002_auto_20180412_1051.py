# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='student',
            field=models.ForeignKey(to='indis.Student'),
        ),
        migrations.AlterField(
            model_name='project',
            name='leader',
            field=models.ForeignKey(to='indis.Student'),
        ),
    ]
