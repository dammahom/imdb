# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(verbose_name='email address', unique=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(null=True, upload_to='items', blank=True)),
                ('total_rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(to='imdb.Item'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='watch_list',
            field=models.ManyToManyField(to='imdb.Item', related_name='user_watch'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wish_list',
            field=models.ManyToManyField(to='imdb.Item', related_name='user_wish'),
        ),
    ]
