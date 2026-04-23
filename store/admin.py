from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Custumer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone']
    list_editable=['phone']
    list_per_page=10

# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display=['placed_at']
#     list_per_page=10

admin.site.register(models.Collection)
# admin.site.register(models.Custumer)

admin.site.register(models.Order)