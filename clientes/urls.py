from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'clientes.views.clientes', name='clientes'),	
	url(r'^perfil/(?P<cliente_id>[-\w]+)$', 'clientes.views.cliente', name='cliente'),
	url(r'^add-representante/(?P<cliente_id>[-\w]+)$', 'clientes.views.add_representante', name='add-representante'),
	url(r'^add-cliente$', 'clientes.views.add_cliente', name='add-cliente'), 
	
)