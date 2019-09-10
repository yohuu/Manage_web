# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('progress', models.CharField(max_length=50)),
                ('budget', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='leader',
            field=models.OneToOneField(to='indis.Student'),
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(to='indis.Project'),
        ),
        migrations.AddField(
            model_name='module',
            name='student',
            field=models.OneToOneField(to='indis.Student'),
        ),
    ]
