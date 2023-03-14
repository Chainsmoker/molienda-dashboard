from django.contrib import admin
from .models import Cliente

# Register your models here.
admin.site.register(Cliente)
admin.site.site_header = "Dashboard - Molienda"