from django.contrib import admin
from .models import demoscale
# Register your models here.
class Scaleadmin(admin.ModelAdmin):
    list_display = ('scale_id','name')
    search_fields = ['name']
    list_filter = ('scale_id','name')
admin.site.register(demoscale, Scaleadmin)