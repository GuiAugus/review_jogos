from django.shortcuts import get_object_or_404, render
from django.views import generic
from jogos.models import Desenvolvedora, Jogo


def index(request):
    num_jogos = Jogo.objects.all().count()
    num_desenvolvedora = Desenvolvedora.objects.count()

    context = {
        'num_jogos' : num_jogos,
        'num_desenvolvedora' : num_desenvolvedora,
    }

    return render(request, 'index.html', context=context)

class JogosListView(generic.ListView):
    model = Jogo
    context_object_name = 'jogo_list'
    template_name = 'jogos/jogos_list.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(JogosListView, self).get_context_data(**kwargs)
        context['some_data'] = 'Teste'
        return context

class JogoDetailView(generic.DetailView):
    model = Jogo

    def jogo_detail_view(request, primary_key):
        jogo = get_object_or_404(Jogo, pk=primary_key)
        return render(request, 'jogos/jogo_detail.html', context={'jogo': jogo})