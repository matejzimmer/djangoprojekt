from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ctenar, Knihovna

def index(request):
    context = {
        'ctenari': Ctenar.objects.all(),
        'knihovny': Knihovna.objects.all()
    }
    return render(request, 'index.html', context=context)

class CtenarListView(ListView):
    model = Ctenar
    template_name = 'ctenari/ctenari_list.html'
    context_object_name = 'ctenari'
    ordering = ['uzivatelske_jmeno']

class CtenarDetailView(DetailView):
    model = Ctenar
    template_name = 'ctenari/ctenari_detail.html'
    context_object_name = 'ctenar'

class KnihovnaListView(ListView):
    model = Knihovna
    template_name = 'knihovny/knihovny_list.html'
    context_object_name = 'knihovny'
    ordering = ['nazev']

class KnihovnaDetailView(DetailView):
    model = Knihovna
    template_name = 'knihovny/knihovny_detail.html'
    context_object_name = 'knihovna'
    pk_url_kwarg = 'pk'

