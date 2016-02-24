# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20160220_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='represntante',
        ),
        migrations.AddField(
            model_name='representante',
            name='proveedor',
            field=models.ForeignKey(to='proveedores.Proveedor', null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='imagen',
            field=models.ImageField(default=b'images/proveedores/default-01.png', upload_to=b'images/proveedores', null=True, verbose_name=b'Imagen Proveedor', blank=True),
        ),
    ]
