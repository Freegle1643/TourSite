from django.contrib import admin
from .models import Touruser, Tourdest, Tourspot
from .models import Tourtrip, Tourjournal
from django.contrib.auth.models import User

# If time permits, do please add User and Touruser to adminsite

# class TouruserAdmin(admin.ModelAdmin):
#     list_display = (User,  usign, ulocation, ujointime, utag)

# class TourdestAdmin(admin.ModelAdmin):
#     list_display = ['dname', 'drealweather']
#
# class Tourjournal(admin.ModelAdmin):
#     list_display = ['jname', 'juser', 'jtag']
#
# class Tourspot(admin.ModelAdmin):
#     list_display = ['sname', 'sdest']
#
# class Tourtrip(admin.ModelAdmin):
#     list_display = ['tname', 'tdays', 'tpeople', 'tdest', 'tspot']

# Register your models here.
admin.site.register(Touruser)
admin.site.register(Tourdest)
admin.site.register(Tourspot)
admin.site.register(Tourtrip)
admin.site.register(Tourjournal)
