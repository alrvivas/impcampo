# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egreso',
            name='archivo',
            field=models.FileField(upload_to=b'archivos/egresos', null=True, verbose_name=b'Archivos', blank=True),
        ),
    ]
