# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20160220_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(null=True)),
                ('fecha_factura', models.DateField(null=True)),
                ('fecha_pago', models.DateField(null=True)),
                ('no_factura', models.CharField(max_length=15, null=True)),
                ('sub_total', models.DecimalField(max_digits=30, decimal_places=3)),
                ('total', models.DecimalField(max_digits=30, decimal_places=3)),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Archivos', blank=True)),
                ('proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
        ),
    ]
