from django.db import models
from django.forms import model_to_dict
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, null=False, blank=False)
    #desc = models.TextField(max_length=500, null=True, blank=True, verbose_name='Descripción')
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Replacement(models.Model):
    
    code_replacement = models.CharField(max_length=150, verbose_name='Código', unique=True, null=True, blank=False)
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, null=True, blank=False)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        return item

    class Meta:
        verbose_name = 'Repuestos'
        verbose_name_plural = 'Repuestos'
        ordering = ['id']
