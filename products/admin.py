from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass

admin.site.register(Image)
