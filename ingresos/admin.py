from django.contrib import admin
from .models import Ingreso

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
	list_display 	= ('id','no_factura','cliente','sub_total','total')
