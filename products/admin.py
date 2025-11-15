from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, TabularInline
from .models import *

class ImageInline(TabularInline):
    model = Image
    extra = 1
    fields = ['image', 'order']
    show_change_link = True

@admin.register(Product)
class ProductAdmin(ModelAdmin, TranslationAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name_ru', 'price', 'category')
    list_filter = ('category',)
    

admin.site.register(Image)
