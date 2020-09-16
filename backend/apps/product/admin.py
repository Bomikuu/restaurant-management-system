from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    exclude = ['deleted_at']


admin.site.register(Product, ProductAdmin)
