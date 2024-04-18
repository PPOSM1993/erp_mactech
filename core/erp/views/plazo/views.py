from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.erp.mixins import IsSuperUserMixin, ValidatePermissionRequiredMixin
from core.erp.models import *
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#from core.erp.forms import CategoryForm


from django.contrib.auth.mixins import LoginRequiredMixin


class PlazoEntregaListView(LoginRequiredMixin, IsSuperUserMixin, ValidatePermissionRequiredMixin, ListView):
    
    model = PlazoEntrega 
    template_name = "plazo/list.html"
    permission_required = 'erp.view_plazo_entrega'
    
    
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
                for i in PlazoEntrega.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position+=1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Plazos de Entrega'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context