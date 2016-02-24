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
from clientes.models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

@login_required(login_url='/login/')
def add_ingreso(request):
    page_title = "Añadir Ingreso"
    user = request.user
    ingreso = Ingreso.objects.all()
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form_ingreso = ingresoForm(request.POST,request.FILES)
        if form_ingreso.is_valid():
            ingreso = form_ingreso.save(commit = False)
            ingreso.save()            
            return redirect(ingreso.get_absolute_url())
    else:
        form_ingreso = ingresoForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-ingreso.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ingresos(request):
    page_title = "Ingresos"
    user = request.user
    ingresos = Ingreso.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(cliente__icontains=query) | Q(no_factura__icontains=query)
        )    
        results = Ingreso.objects.filter(qset).order_by('-id')
        template_name = "resultados-ingresos.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="ingresos.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def ingreso(request,ingreso_id):
    user = request.user
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)  
    page_title = ingreso.cliente     
    template_name ="ingreso.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_ingreso(request,ingreso_id):
    page_title = "Editat Ingreso"
    user = request.user
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)    
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        form_ingreso = ingresoForm(request.POST,request.FILES,instance=ingreso)
        if form_ingreso.is_valid():
            ingreso = form_ingreso.save(commit = False)
            ingreso.save()            
            return redirect(ingreso.get_absolute_url())
    else:
        form_ingreso = ingresoForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-ingreso.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))