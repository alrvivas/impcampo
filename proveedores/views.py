# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

@login_required(login_url='/login/')
def add_proveedor(request):
    page_title = "Añadir Proveedor"
    user = request.user
    proveedor = Proveedor.objects.all()
    if request.method == 'POST':
        form_proveedor = proveedorForm(request.POST,request.FILES)
        if form_proveedor.is_valid():
            proveedor = form_proveedor.save(commit = False)
            proveedor.save()            
            return redirect(proveedor.get_absolute_url())
    else:
        form_proveedor = proveedorForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-proveedor.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def proveedores(request):
    page_title = "Proveedores"
    user = request.user
    proveedores = Proveedor.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre_comercial__icontains=query) | Q(nombre_fiscal__icontains=query)
        )    
        results = Proveedor.objects.filter(qset).order_by('-id')
        template_name = "resultados-proveedor.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="proveedores.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def proveedor(request,proveedor_id):
    user = request.user
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    representantes = Representante.objects.filter(proveedor=proveedor)    
    page_title = proveedor.nombre_comercial     
    template_name ="proveedor.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_representante(request,proveedor_id):
    user = request.user
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    page_title = proveedor.nombre_comercial 
    representante = Representante.objects.all()
    if request.method == 'POST':
        form_representante = representanteForm(request.POST)
        if form_representante.is_valid():
            representante = form_representante.save(commit = False)
            representante.save()            
            return redirect(proveedor.get_absolute_url())
    else:
        form_representante = representanteForm()
    args = {}
    args.update(csrf(request))    
    template_name ="add-representante.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_proveedor(request,proveedor_id):
    page_title = "Editat Proveedor"
    user = request.user
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form_proveedor = proveedorForm(request.POST,request.FILES,instance=proveedor)
        if form_proveedor.is_valid():
            proveedor = form_proveedor.save(commit = False)
            proveedor.save()            
            return redirect(proveedor.get_absolute_url())
    else:
        form_proveedor = clienteForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-proveedor.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))