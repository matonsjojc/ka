from django.contrib import admin
from ka.models import Pacient

class PacientAdmin(admin.ModelAdmin):
    list_display = ('ime', 'aparat')

admin.site.register(Pacient, PacientAdmin)
