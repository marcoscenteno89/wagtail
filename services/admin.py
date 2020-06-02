from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Product, Promotion, CompanyPage

class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = 'Products'
    menu_icon = 'placeholder'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'company', 'service_type',)
    search_fields = ('title', 'company', 'service_type',)


class PromotionAdmin(ModelAdmin):
    model = Promotion
    menu_label = 'Promotions'
    menu_icon = 'placeholder'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'company',)
    search_fields = ('title', 'company',)


class CompanyAdmin(ModelAdmin):
    model = CompanyPage
    menu_label = 'Companies'
    menu_icon = 'placeholder'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    search_fields = ('title',)


modeladmin_register(PromotionAdmin)
modeladmin_register(ProductAdmin)
modeladmin_register(CompanyAdmin)