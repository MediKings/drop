from django.contrib import admin
from .models import Category, SubCategory, Product, Order


class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SubCategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategorieAdmin)
admin.site.register(SubCategory, SubCategorieAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
