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
from proveedores.models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

@login_required(login_url='/login/')
def add_egreso(request):
    page_title = "Añadir Egreso"
    user = request.user
    egreso = Egreso.objects.all()
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form_egreso = egresoForm(request.POST,request.FILES)
        if form_egreso.is_valid():
            egreso = form_egreso.save(commit = False)
            egreso.save()            
            return redirect(egreso.get_absolute_url())
    else:
        form_egreso = egresoForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-egreso.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def egresos(request):
    page_title = "Egresos"
    user = request.user
    egresos = Egreso.objects.all()    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(proveedor__icontains=query) | Q(no_factura__icontains=query)
        )    
        results = Egreso.objects.filter(qset).order_by('-id')
        template_name = "resultados-egresos.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="egresos.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def egreso(request,egreso_id):
    user = request.user
    egreso = get_object_or_404(Egreso, id=egreso_id)  
    page_title = egreso.proveedor     
    template_name ="egreso.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def edit_egreso(request,egreso_id):
    page_title = "Editat Egreso"
    user = request.user
    egreso = get_object_or_404(Egreso, id=egreso_id)    
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form_egreso = egresoForm(request.POST,request.FILES,instance=egreso)
        if form_egreso.is_valid():
            egreso = form_egreso.save(commit = False)
            egreso.save()            
            return redirect(egreso.get_absolute_url())
    else:
        form_egreso = egresoForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-egreso.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def graficar_egreso(request):
    user = request.user
    egresosdata = \
        DataPool(
           series=
            [{'options': {
               'source': Egreso.objects.all()},
              'terms': [
                'fecha_registro',
                'total']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = egresosdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'fecha_registro': [
                    'total']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Grafica de Egresos'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})
    template_name ="graficar-egreso.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))