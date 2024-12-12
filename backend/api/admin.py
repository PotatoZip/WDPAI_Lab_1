from django.contrib import admin
from .models import SystemUser, BusinessUser  

# Register your models here.

admin.site.register(SystemUser)
admin.site.register(BusinessUser)