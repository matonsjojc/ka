from django.contrib import admin
from ka.models import Pacient, Ponudnik, Aparat, Maska, Vprasanje, Odgovor, Anketa

class AparatInline(admin.StackedInline):
    model = Aparat
    extra = 0

class MaskaInline(admin.StackedInline):
    model = Maska
    extra = 0

class OdgovorInline(admin.StackedInline):
    model = Odgovor
    extra = 0

class PacientAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'ime', 'ponudnik')
    fields = ['user', 'ponudnik', 'ime']
    inlines = [
        AparatInline,
        MaskaInline,
    ]

class PonudnikAdmin(admin.ModelAdmin):
    pass

class AparatAdmin(admin.ModelAdmin):
    list_display = ('pacient', 'proizvajalec')

class MaskaAdmin(admin.ModelAdmin):
    list_display = ('pacient', 'name')

class VprasanjeAdmin(admin.ModelAdmin):
    list_display = ('tekst', 'komentar_k_tekstu', 'aktiven')
    fields = ['tekst']
    inlines = [
        OdgovorInline,
    ]

admin.site.register(Pacient, PacientAdmin)
admin.site.register(Ponudnik, PonudnikAdmin)
admin.site.register(Aparat, AparatAdmin)
admin.site.register(Maska, MaskaAdmin)
admin.site.register(Vprasanje, VprasanjeAdmin)
admin.site.register(Odgovor)
admin.site.register(Anketa)
