from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'proveedores.views.proveedores', name='proveedores'),	
	url(r'^perfil/(?P<proveedor_id>[-\w]+)$', 'proveedores.views.proveedor', name='proveedor'),
	url(r'^add-representante/(?P<proveedor_id>[-\w]+)$', 'proveedores.views.add_representante', name='add-representante'),
	url(r'^add-proveedor/$', 'proveedores.views.add_proveedor', name='add-proveedor'),
	url(r'^editar-proveedor/(?P<proveedor_id>[-\w]+)$', 'proveedores.views.edit_proveedor', name='editar-proveedor'),
	
)