from django.db import transaction
import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.erp.mixins import IsSuperUserMixin, ValidatePermissionRequiredMixin
from core.erp.models import *
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.erp.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class CotizacionListView(LoginRequiredMixin, IsSuperUserMixin, ValidatePermissionRequiredMixin, ListView):
    model = Cotizacion
    template_name = 'cotizacion/list.html'
    permission_required = 'erp.view_cotizacion'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Cotizaciones'
        context['create_url'] = reverse_lazy('erp:cotizacion_create')
        context['list_url'] = reverse_lazy('erp:cotizacion_list')
        context['entity'] = 'Cotizaciones'
        return context


class CotizacionCreateView(LoginRequiredMixin, IsSuperUserMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'cotizacion/create.html'
    success_url = reverse_lazy('erp:cotizacion_list')
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_cotizacion'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Cotización'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = reverse_lazy('erp:cotizacion_list')
        context['action'] = 'add'
        return context