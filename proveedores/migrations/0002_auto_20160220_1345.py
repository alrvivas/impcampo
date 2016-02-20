# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='dias_credito',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='imagen',
            field=models.ImageField(default=b'images/empleados/default-01.png', upload_to=b'images/empleados', null=True, verbose_name=b'Imagen Proveedor', blank=True),
        ),
    ]
