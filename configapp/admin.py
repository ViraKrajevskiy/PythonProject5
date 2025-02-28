from django.contrib import admin
from configapp.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','birthdate','created_at','updated_at')
    list_display_links = ['name']
    search_fields = ['name']
    list_editable = ['is_bool']

admin.site.register([Actor,Movie])

