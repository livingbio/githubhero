# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('event', models.ForeignKey(to='github.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contributions', jsonfield.fields.JSONField(default=b'{}')),
                ('repo', models.ForeignKey(to='github.Repository')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='role',
            name='user',
            field=models.ForeignKey(to='github.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('repo', 'user')]),
        ),
        migrations.AddField(
            model_name='eventcount',
            name='repo',
            field=models.ForeignKey(to='github.Repository'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventcount',
            name='user',
            field=models.ForeignKey(to='github.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='eventcount',
            unique_together=set([('repo', 'user', 'event')]),
        ),
    ]
