from django.contrib import admin
from .models import Egreso

@admin.register(Egreso)
class EgresoAdmin(admin.ModelAdmin):
	list_display 	= ('id','no_factura','proveedor','sub_total','total')