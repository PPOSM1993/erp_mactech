from django.urls import path

from core.erp.views.category.views import *
from core.erp.views.replacement.views import *
from core.erp.views.dashboard.views import DashboardView

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
]