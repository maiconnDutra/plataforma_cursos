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