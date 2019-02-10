# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='', to='blog.Category'),
            preserve_default=False,
        ),
    ]
