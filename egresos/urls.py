from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'egresos.views.egresos', name='egresos'),	
	url(r'^egreso/(?P<egreso_id>[-\w]+)$', 'egresos.views.egreso', name='egreso'),
	url(r'^add-egreso/$', 'egresos.views.add_egreso', name='add-egreso'),
	url(r'^editar-egresos/(?P<egreso_id>[-\w]+)$', 'egresos.views.edit_egreso', name='editar-egreso'),
	url(r'^graficar/$', 'egresos.views.graficar_egreso', name='graficar-egreso'),
	
)