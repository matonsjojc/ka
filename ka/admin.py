from django.contrib import admin
from ka.models import Pacient, Ponudnik

class PacientAdmin(admin.ModelAdmin):
    list_display = ('user', 'ime', 'ponudnik')

class PonudnikAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pacient, PacientAdmin)
admin.site.register(Ponudnik, PonudnikAdmin)
