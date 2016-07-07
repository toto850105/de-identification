# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('dp_id', models.AutoField(primary_key=True, serialize=False)),
                ('privacy_level', models.PositiveSmallIntegerField(default=0)),
                ('epsilon', models.FloatField()),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('synthetic_path', models.CharField(blank=True, max_length=300)),
                ('statistics_err', models.TextField(blank=True)),
                ('log_path', models.CharField(blank=True, max_length=300)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ('start_time',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('data_path', models.CharField(max_length=300)),
                ('selected_attrs', models.TextField()),
                ('jtree_strct', models.TextField(blank=True, max_length=500)),
                ('dep_graph', models.TextField(blank=True)),
                ('valbin_map', models.TextField(blank=True)),
                ('domain', models.TextField(blank=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'WAITTING'), (1, 'FINISH'), (2, 'ERROR')], default=0)),
            ],
            options={
                'ordering': ('start_time',),
            },
        ),
        migrations.AddField(
            model_name='job',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Task'),
        ),
    ]
