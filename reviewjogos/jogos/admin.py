from django.contrib import admin
from jogos.models import Desenvolvedora, Genero, Jogo, Plataforma


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'lancamento', 'plataforma')

@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    pass

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    pass