from django.contrib import admin
from .models import weith
# Register your models here.
class Weightadmin(admin.ModelAdmin):
    list_display= ('weight_id','scale_id', 'unit_weight','weight_current', 'number')
    search_fields = ['weight_id']
    list_filter = ('weight_id','scale_id', 'unit_weight','weight_current', 'number')
admin.site.register(weith, Weightadmin)