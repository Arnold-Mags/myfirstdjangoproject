from django.contrib import admin
from .models import SystemUser

admin.site.site_header = "System User Admin"
admin.site.site_title = "System User Admin Portal"
admin.site.index_title = "Welcome to System User Portal"

class SystemUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'image_tag', 'contact_number', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('created_at',)
    ordering = ('username',)


admin.site.register(SystemUser, SystemUserAdmin)