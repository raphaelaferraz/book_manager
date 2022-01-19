from django.shortcuts import render, get_object_or_404
from .models import Livros


def index(request):
    livros = Livros.objects.order_by('nome_do_livro').all()

    dados = {
        'livros': livros
    }

    return render(request, 'index.html', dados)


def buscar(request):
    lista_livros = Livros.objects.all()

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']

        if buscar:
            lista_livros = lista_livros.filter(nome_do_livro__icontains=nome_a_buscar)

    dados = {
        'livros': lista_livros
    }

    return render(request, 'buscar.html', dados)


def livro(request, id_livro):

    livro_a_exibir = {
        'livro': get_object_or_404(Livros, pk=id_livro)
    }

    return render(request, 'livro.html', livro_a_exibir)
