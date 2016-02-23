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

def LoginView(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    return render_to_response('inactivousuario.html', context_instance=RequestContext(request))#no activo
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))#no usuario
    else:
        formulario = AuthenticationForm()
    page_title = "Ingreso de Usuarios"
    return render_to_response('login.html',{'formulario':formulario,'page_title':page_title}, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
def index(request):
    page_title = "Ingresos Egresos CA"
    user = request.user    
    template_name ="index.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 


@login_required(login_url='/login/')
def add_cliente(request):
    page_title = "Añadir Cliente"
    user = request.user
    cliente = Cliente.objects.all()
    if request.method == 'POST':
        form_cliente = clienteForm(request.POST,request.FILES)
        if form_cliente.is_valid():
            cliente = form_cliente.save(commit = False)
            cliente.save()            
            return redirect(cliente.get_absolute_url())
    else:
        form_cliente = clienteForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-cliente.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def clientes(request):
    page_title = "Clientes"
    user = request.user
    users = User.objects.all()
    clientes = Cliente.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre_comercial=query) | Q(nombre_fiscal=query)
        )    
        results = Empleado.objects.filter(qset).order_by('-id')
        template_name = "resultados-cliente.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="clientes.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def cliente(request,cliente_id):
    user = request.user
    cliente = get_object_or_404(Cliente, id=cliente_id)
    representantes = Representante.objects.filter(cliente=cliente)    
    page_title = cliente.nombre_comercial     
    template_name ="cliente.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_representante(request,cliente_id):
    user = request.user
    cliente = get_object_or_404(Cliente, id=cliente_id)
    page_title = cliente.nombre_comercial 
    representante = Representante.objects.all()
    if request.method == 'POST':
        form_representante = representanteForm(request.POST)
        if form_representante.is_valid():
            representante = form_representante.save(commit = False)
            representante.save()            
            return redirect(cliente.get_absolute_url())
    else:
        form_representante = representanteForm()
    args = {}
    args.update(csrf(request))    
    template_name ="add-representante.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_cliente(request,cliente_id):
    page_title = "Editat Cliente"
    user = request.user
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form_cliente = clienteForm(request.POST,request.FILES,instance=cliente)
        if form_cliente.is_valid():
            cliente = form_cliente.save(commit = False)
            cliente.save()            
            return redirect(cliente.get_absolute_url())
    else:
        form_cliente = clienteForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-cliente.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))