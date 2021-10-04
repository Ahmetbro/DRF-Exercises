from django.contrib import admin
from .models import Certificate
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','created_at', 'updated_at')
    search_fields = ('name',)
    


admin.site.register(Certificate, CertificateAdmin)