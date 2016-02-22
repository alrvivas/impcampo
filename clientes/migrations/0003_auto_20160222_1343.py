# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20160220_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='represntante',
            field=models.ForeignKey(to='clientes.Representante', null=True),
        ),
    ]
