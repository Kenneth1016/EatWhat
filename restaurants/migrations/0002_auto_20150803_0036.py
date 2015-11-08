# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createId', models.CharField(max_length=20)),
                ('createAt', models.DateField()),
                ('valid', models.BooleanField(default=True)),
                ('memo', models.CharField(max_length=200, blank=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('money', models.DecimalField(max_digits=5, decimal_places=0)),
                ('food', models.ForeignKey(to='restaurants.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderDate', models.DateField()),
                ('createId', models.CharField(max_length=20)),
                ('createAt', models.DateField()),
                ('valid', models.BooleanField(default=True)),
                ('orderable', models.BooleanField(default=True)),
                ('memo', models.CharField(max_length=200, blank=True)),
                ('restaurant', models.ForeignKey(to='restaurants.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='orderMain',
            field=models.ForeignKey(to='restaurants.OrderMain'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='food',
            name='Memo',
        ),
        migrations.AddField(
            model_name='food',
            name='memo',
            field=models.CharField(default=datetime.datetime(2015, 8, 2, 16, 36, 42, 756072, tzinfo=utc), max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='memo',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
