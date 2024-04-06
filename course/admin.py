from django.contrib import admin
from . models import USerMaster
# Register your models here.

class YourModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','date_of_birth','city','my_field']  # Display all fields

admin.site.register(USerMaster, YourModelAdmin)