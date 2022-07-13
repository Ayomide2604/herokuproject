from django.contrib import admin
from.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    prepopulated_fields = {
        'slug': ('name',)
    }

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'in_stock', 'date_created', 'slug', )
    list_editable = ('price', 'in_stock',)
    list_display_links = ('name', 'id', )
    prepopulated_fields= {'slug': ('name',)}

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')




admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(UserItem)

