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



class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('erp:sale_list')
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_sale'
    url_redirect = success_url


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Venta'
        context['entity'] = 'Ventas'
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['action'] = 'add'
        return context


"""

   model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('erp:sale_list')
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_replacements':
                data = []
                replacement = Replacement.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in replacement:
                    item = i.toJSON()
                    #item['value'] = i.code_replacement
                    item['value'] = i.name + " - " + i.code_replacement
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Sale()
                    sale.date_joined = vents['date_joined']
                    sale.cli_id = vents['cli']
                    sale.pay_method_id = vents['pay_method']
                    sale.subtotal = float(vents['subtotal'])
                    sale.iva = float(vents['iva'])
                    sale.total = float(vents['total'])
                    print(vents)
                    sale.save()
                    
                    for i in vents['replacement']:
                        det = DetSale()
                        det.sale_id = sale.id
                        det.replacement_id = i['id']
                        det.pay_method_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['pvp'])
                        det.cant = int(i['cant'])
                        det.subtotal = float(i['subtotal'])
                        det.save()

            else:
                data['error'] = "No ha ingresado a un ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Cotización'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['action'] = 'add'
        return context


"""



"""class SaleListView(LoginRequiredMixin, IsSuperUserMixin, ValidatePermissionRequiredMixin, ListView):
    model = Sale
    template_name = 'sale/list.html'
    permission_required = 'erp.view_sale'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Sale.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            elif action == 'search_details_replacement':
                data = []
                position = 1
                for i in DetSale.objects.filter(sale_id=request.POST['id']):
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista Cotizaciones'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['entity'] = 'Cotizaciones'
        return context


 class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('erp:sale_list')
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_replacements':
                data = []
                replacement = Replacement.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in replacement:
                    item = i.toJSON()
                    #item['value'] = i.code_replacement
                    item['value'] = i.name + " - " + i.code_replacement
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Sale()
                    sale.date_joined = vents['date_joined']
                    sale.cli_id = vents['cli']
                    sale.pay_method_id = vents['pay_method']
                    sale.subtotal = float(vents['subtotal'])
                    sale.iva = float(vents['iva'])
                    sale.total = float(vents['total'])
                    print(vents)
                    sale.save()
                    
                    for i in vents['replacement']:
                        det = DetSale()
                        det.sale_id = sale.id
                        det.replacement_id = i['id']
                        det.pay_method_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['pvp'])
                        det.cant = int(i['cant'])
                        det.subtotal = float(i['subtotal'])
                        det.save()

            else:
                data['error'] = "No ha ingresado a un ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Cotización'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['action'] = 'add'
        return context



class SaleDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Sale
    template_name = 'sale/delete.html'
    success_url = reverse_lazy('erp:sale_list')
    permission_required = 'erp.delete_sale'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cotización'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = self.success_url
        return context

"""
