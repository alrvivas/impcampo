from django.contrib import admin
from .models import Cliente,Representante

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre_fiscal',)

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)
