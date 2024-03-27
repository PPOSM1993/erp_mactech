from django.urls import path

from core.erp.views.category.views import *

from core.erp.views.replacement.views import *

from core.erp.views.client.views import *

from core.erp.views.dashboard.views import DashboardView

from core.erp.views.sale.views import *


app_name = 'erp'

urlpatterns = [
    #Category
    path('category/list/', CategoryListView.as_view(), name="category_list"),
    path('category/add/', CategoryCreateView.as_view(), name="category_create"),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name="category_update"),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name="category_delete"),
        
    #Replacement
    path('replacement/list/', ReplacementListView.as_view(), name="replacement_list"),
    path('replacement/add/', ReplacementCreateView.as_view(), name="replacement_create"),
    path('replacement/update/<int:pk>/', ReplacementUpdateView.as_view(), name="replacement_update"),
    path('replacement/delete/<int:pk>/', ReplacementDeleteView.as_view(), name="replacement_delete"),
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    #Customer
    path('client/list/', ClientListView.as_view(), name="client_list"),
    path('client/add/', ClientCreateView.as_view(), name="client_create"),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name="client_update"),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name="client_delete"),
    
    #Sale
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
]