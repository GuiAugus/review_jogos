from django.shortcuts import render
from jogos.models import Desenvolvedora, Jogo


def index(request):
    num_jogos = Jogo.objects.all().count()
    num_desenvolvedora = Desenvolvedora.objects.count()

    context = {
        'num_jogos' : num_jogos,
        'num_desenvolvedora' : num_desenvolvedora,
    }

    return render(request, 'index.html', context=context)