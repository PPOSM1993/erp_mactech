from django.views.generic import TemplateView #,View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.erp.models import *


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['category'] = Category.objects.all().count()
        context['replacement'] = Replacement.objects.all().count()
        #context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context