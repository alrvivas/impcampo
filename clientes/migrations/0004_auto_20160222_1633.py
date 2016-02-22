# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20160222_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(default=b'images/clientes/default-01.png', upload_to=b'images/clientes', null=True, verbose_name=b'Imagen Cliente', blank=True),
        ),
    ]
