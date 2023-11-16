from django.contrib import admin
from .models import Montadora, Itens, Carro, Nome


admin.site.register(Montadora)
admin.site.register(Itens)
admin.site.register(Carro)
admin.site.register(Nome)