from django.contrib import admin

from apps.waitlist.models import WaitlistEntry

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name','created_at', 'updated_at')
    search_fields = ('first_name','last_name')
    

admin.site.register(WaitlistEntry)