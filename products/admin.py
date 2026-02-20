from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
