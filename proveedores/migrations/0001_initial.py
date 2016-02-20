# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(null=True)),
                ('nombre_fiscal', models.CharField(max_length=140, null=True)),
                ('nombre_comercial', models.CharField(max_length=140, null=True)),
                ('direccion', models.CharField(max_length=140, null=True)),
                ('rfc', models.CharField(max_length=20, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('imagen', models.ImageField(default=b'images/empleados/default-01.png', upload_to=b'images/empleados', null=True, verbose_name=b'Imagen Empleado', blank=True)),
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
        migrations.AddField(
            model_name='proveedor',
            name='represntante',
            field=models.ForeignKey(to='proveedores.Representante'),
        ),
    ]
