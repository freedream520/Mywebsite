# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
