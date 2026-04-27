from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Custumer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['get_first_name', 'get_last_name', 'get_email','phone']
    list_editable=['phone']
    list_per_page=10

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display=['placed_at']
#     list_per_page=10

admin.site.register(models.Collection)
# admin.site.register(models.Custumer)

admin.site.register(models.Order)