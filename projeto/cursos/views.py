from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Curso

class CursoCreateView(CreateView):
    model = Curso
    fields = ['titulo', 'descricao', 'preco', 'carga_horaria', 'nivel', 'capa_url']
    success_url = reverse_lazy('curso_list')

class CursoListView(ListView):
    model = Curso
    context_object_name = 'cursos'

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['titulo', 'descricao', 'preco', 'carga_horaria', 'nivel', 'capa_url']
    success_url = reverse_lazy('curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('curso_list')

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/curso_detail.html'
    context_object_name = 'curso'