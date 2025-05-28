from urllib.parse import parse_qs, urlparse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Curso, Aula

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

class AulaCreateView(CreateView):
    model = Aula
    fields = ['curso', 'titulo', 'descricao', 'video_url']
    template_name = 'cursos/aula_form.html'

    def get_initial(self):
        initial = super().get_initial()
        curso_id = self.request.GET.get('curso') or self.kwargs.get('curso_id')
        if curso_id:
            initial['curso'] = curso_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['curso_id'] = self.request.GET.get('curso') or self.kwargs.get('curso_id')
        return context

    def get_success_url(self):
        return reverse_lazy('curso_detail', kwargs={'pk': self.object.curso.pk})
    
class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['curso', 'titulo', 'descricao', 'video_url']
    template_name = 'cursos/aula_form.html'

    def get_initial(self):
        initial = super().get_initial()
        curso_id = self.request.GET.get('curso')
        if curso_id:
            initial['curso'] = curso_id
        return initial

    def get_success_url(self):
        return reverse_lazy('curso_detail', kwargs={'pk': self.object.curso.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['curso_id'] = self.request.GET.get('curso') or (self.object.curso.pk if self.object else None)
        return context

class AulaDeleteView(DeleteView):
    model = Aula
    template_name = 'cursos/aula_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('curso_detail', kwargs={'pk': self.object.curso.pk})
    
def video_player(request):
    original_url = request.GET.get('url', '')
    embed_url = original_url

    if "youtube.com/watch" in original_url:
        video_id = parse_qs(urlparse(original_url).query).get("v")
        if video_id:
            embed_url = f"https://www.youtube.com/embed/{video_id[0]}"

    return render(request, 'cursos/video_player.html', {'video_url': embed_url})