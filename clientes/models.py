from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Representante(models.Model):
	nombre 	= models.CharField(max_length=140)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)

	def __unicode__(self): 
		return unicode(self.nombre)

class Cliente(models.Model):
	represntante = models.ForeignKey(Representante,null=True)
	fecha_registro = models.DateField(null=True)	
	nombre_fiscal = models.CharField(max_length=140,null=True)
	nombre_comercial = models.CharField(max_length=140,null=True)
	direccion = models.CharField(max_length=140,null=True)
	rfc = models.CharField(max_length=20,null=True)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)
	dias_credito = models.PositiveIntegerField(null=True)	
	imagen = models.ImageField("Imagen Cliente", upload_to="images/clientes", blank=True, null=True,default='images/clientes/default-01.png')
	
	@models.permalink
	def get_absolute_url(self):
		return('cliente', (), { 'cliente_id': self.id })

	def __unicode__(self):
		return unicode(self.nombre_comercial)


