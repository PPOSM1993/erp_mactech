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

class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create.html'
    #success_url = reverse_lazy('erp:sale_list')
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
            if action == 'search_replacement':
                data = []
                replacement = Replacement.objects.filter( name__icontains=request.POST['term'])[0:10]
                for i in replacement:
                    item = i.toJSON()
                    #item['value'] = i.code_replacement
                    item['value'] = i.name + " - " + i.code_replacement
                    
                    data.append(item)
                    
            #if action == 'add':
            #    form = self.get_form()
            #    data = form.save()
            else:
                data['error'] = "No ha ingresado a un ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación Venta'
        context['entity'] = 'Ventas'
        #context['list_url'] = self.success_url
        context['action'] = 'add'
        return context