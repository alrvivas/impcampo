from django.contrib import admin
from .models import Proveedor,Representante

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre_fiscal',)

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)
