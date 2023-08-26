from django.contrib import admin
from.models import OurModel
from.forms import Ourforms
class OurAdmin(admin.ModelAdmin):
    form = Ourforms
    list_display = ("name",'fname')
    search_fields = ('name',)
admin.site.register(OurModel,OurAdmin)