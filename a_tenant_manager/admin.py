from django.contrib import admin
from .models import *

# Register your models here.

class TenantAdminSite(admin.AdminSite):
    site_header = "Tenant Admin"
    site_title = "Tenant Admin Portal"
    index_title = "Welcome to Tenant Admin Portal"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(Tenant)
        self.register(Domain)

tenant_admin_site = TenantAdminSite(name='tenant_admin_site')
