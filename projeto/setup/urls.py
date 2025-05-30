"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cursos.views import CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView, CursoDetailView, AulaCreateView, AulaUpdateView, AulaDeleteView, video_player

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('novo/', CursoCreateView.as_view(), name='curso_create'),
    path('editar/<int:pk>/', CursoUpdateView.as_view(), name='curso_update'),
    path('excluir/<int:pk>/', CursoDeleteView.as_view(), name='curso_delete'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso_detail'),
    path('curso/<int:curso_id>/aula/novo/', AulaCreateView.as_view(), name='aula_create_com_curso'),
    path('aula/<int:pk>/editar/', AulaUpdateView.as_view(), name='aula_update'),
    path('aula/<int:pk>/excluir/', AulaDeleteView.as_view(), name='aula_delete'),
    path('assistir/', video_player, name='video_player'),
]
