# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190210_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
