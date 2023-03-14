from django.contrib import admin
from .models import *

# Register your models here.
class MoliendaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "cliente", "kg_estimados", "origen", "guia_recepcion")

admin.site.register(Molienda, MoliendaAdmin)
admin.site.register(MaterialDureza)
admin.site.register(MaterialHumedad)
admin.site.register(MaterialTamaño)
admin.site.register(MaterialSulfuro)
admin.site.register(OrigenMaterial)