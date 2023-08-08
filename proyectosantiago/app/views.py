from django.shortcuts import render, get_object_or_404
from .models import EntradaBlog, Pagina
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EntradaBlog

def lista_entradas(request):
    entradas = EntradaBlog.objects.all()
    return render(request, 'blog_app/lista_entradas.html', {'entradas': entradas})

def detalle_entrada(request, entrada_id):
    entrada = get_object_or_404(EntradaBlog, pk=entrada_id)
    return render(request, 'blog_app/detalle_entrada.html', {'entrada': entrada})

def acerca_de(request):
    return render(request, 'blog_app/acerca_de.html')

@login_required
def crear_entrada(request):
    # Lógica para crear una nueva entrada de blog
    pass

class ActualizarEntradaView(LoginRequiredMixin, UpdateView):
    # Lógica para actualizar una entrada de blog existente
    model = EntradaBlog
    fields = ['titulo', 'contenido', 'fecha_publicacion']
    template_name = 'blog_app/form_entrada.html'

class EliminarEntradaView(LoginRequiredMixin, DeleteView):
    # Lógica para eliminar una entrada de blog
    model = EntradaBlog
    success_url = reverse_lazy('lista_entradas')
