from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'clientes.views.clientes', name='clientes'),	
	url(r'^perfil/(?P<cliente_id>[-\w]+)$', 'clientes.views.cliente', name='cliente'),
	url(r'^add-cliente/(?P<cliente_id>[-\w]+)$', 'clientes.views.add_cliente', name='add-cliente'), 
	
)