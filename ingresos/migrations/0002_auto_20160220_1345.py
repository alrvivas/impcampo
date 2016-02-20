# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Representante',
        ),
        migrations.AddField(
            model_name='ingreso',
            name='fecha_pago',
            field=models.DateField(null=True),
        ),
    ]
