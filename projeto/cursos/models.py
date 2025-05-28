from urllib.parse import parse_qs, urlparse
from django.db import models

NIVEIS = [
    ('iniciante', 'Iniciante'),
    ('intermediario', 'Intermediário'),
    ('avancado', 'Avançado'),
]

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    carga_horaria = models.PositiveIntegerField(help_text="Duração do curso em horas")
    nivel = models.CharField(max_length=20, choices=NIVEIS)
    capa_url = models.URLField(help_text="URL da imagem de capa do curso")
    def __str__(self):
        return self.titulo
    
class Aula(models.Model):
    curso = models.ForeignKey(Curso, related_name='aulas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    video_url = models.URLField(blank=True, help_text="URL do vídeo da aula")

    def __str__(self):
        return self.titulo
    
    def get_youtube_id(self):
        if not self.video_url:
            return ""
        if 'youtu.be/' in self.video_url:
            return self.video_url.split('/')[-1]
        if 'youtube.com' in self.video_url:
            query = urlparse(self.video_url).query
            return parse_qs(query).get('v', [''])[0]
        return ""