from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'ingresos.views.ingresos', name='ingresos'),	
	url(r'^ingreso/(?P<egreso_id>[-\w]+)$', 'egresos.views.ingreso', name='ingreso'),
	url(r'^add-ingreso/$', 'ingresos.views.add_ingreso', name='add-ingreso'),
	url(r'^editar-ingreso/(?P<egreso_id>[-\w]+)$', 'ingresos.views.edit_ingreso', name='editar-ingreso'),
	
)