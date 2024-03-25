from django.forms import ModelForm
from django.forms import *
from core.erp.models import *

class CategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Nombre Categoría',
                    'class': 'form-control form-control-sm'
                }
            )
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ReplacementForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Replacement
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Repuesto',
                    'class': 'form-control form-control-sm'
                }
            ),
            'code_replacement': TextInput(
                attrs={
                    'placeholder': 'Código Respuesto',
                    'class': 'form-control form-control-sm'
                }
            ),
            
            
            'stock': TextInput(
                attrs={
                    'placeholder': '',
                    "type": "number",
                    'class': 'form-control form-control-sm'
                }
            )
                        
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data