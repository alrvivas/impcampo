from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from clientes.models import *

class Ingreso(models.Model):
	cliente = models.ForeignKey(Cliente)
	fecha_registro = models.DateField(null=True)
	fecha_factura = models.DateField(null=True)
	fecha_pago = models.DateField(null=True)	
	no_factura = models.CharField(max_length=15,null=True)
	sub_total = models.DecimalField(max_digits = 30,decimal_places = 3,)
	total = models.DecimalField(max_digits = 30,decimal_places = 3,)
	archivo = models.FileField("Archivos", upload_to="archivos/categorias", blank=True, null=True)


	@models.permalink
	def get_absolute_url(self):
		return('ingreso', (), { 'ingreso_id': self.id })

	def __unicode__(self):
		return unicode(self.id)