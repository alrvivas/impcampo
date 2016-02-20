# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(null=True)),
                ('fecha_factura', models.DateField(null=True)),
                ('no_factura', models.CharField(max_length=15, null=True)),
                ('sub_total', models.DecimalField(max_digits=30, decimal_places=3)),
                ('total', models.DecimalField(max_digits=30, decimal_places=3)),
                ('archivo', models.FileField(upload_to=b'archivos/categorias', null=True, verbose_name=b'Archivos', blank=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
