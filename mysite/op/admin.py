from django.contrib import admin
from .models import Resources
# Register your models here.
#admin.site.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ("name", "ip", "c_time")
    list_filter = ("name", "ip")
    search_fields = ("name", "ip", "c_time")
    date_hierarchy = "c_time"
    #ordering = ["name", "ip"]
admin.site.register(Resources, ResourcesAdmin)
