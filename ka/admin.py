from django.contrib import admin
from ka.models import Pacient, Ponudnik, Aparat, Maska

class PacientAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'ime', 'ponudnik')

class PonudnikAdmin(admin.ModelAdmin):
    pass

class AparatAdmin(admin.ModelAdmin):
    list_display = ('pacient', 'proizvajalec')

class MaskaAdmin(admin.ModelAdmin):
    list_display = ('pacient', 'name')

admin.site.register(Pacient, PacientAdmin)
admin.site.register(Ponudnik, PonudnikAdmin)
admin.site.register(Aparat, AparatAdmin)
admin.site.register(Maska, MaskaAdmin)
