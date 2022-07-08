from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name',)
    list_display_links = ('id', 'email')
admin.site.register(Contact, ContactAdmin)