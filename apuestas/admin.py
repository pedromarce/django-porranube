from django.contrib import admin
from apuestas.models import Usuario, Temporada, Partido, Apuesta

admin.site.register(Usuario)
admin.site.register(Temporada)
admin.site.register(Partido)
admin.site.register(Apuesta)
