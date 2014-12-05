# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141205_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
            preserve_default=True,
        ),
    ]
