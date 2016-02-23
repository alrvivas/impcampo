# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20160222_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='represntante',
        ),
        migrations.AddField(
            model_name='representante',
            name='cliente',
            field=models.ForeignKey(to='clientes.Cliente', null=True),
        ),
    ]
