from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)} #prepopulate)fields is a dictionary, also, slug which is key in dict here, must be the same name as slugfield used in model.py, where to use - as we have prepopulated category_name in slug, then what actually happens is that when we type category_name hand in hand slug field will also automatically type the same name as category_name in the categorys table in the backend, except the first char will always be small letter in prepopulate field.
    list_display = ('category_name', 'slug')  #it displays the lst in the category that is to be shown in front.

admin.site.register(Category, CategoryAdmin)