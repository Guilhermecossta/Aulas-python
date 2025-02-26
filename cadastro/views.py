from django.shortcuts import render
from django.http import JsonResponse
from cadastro.models import Estudante,Curso
from cadastro.serializers import EstudanteSerializer,CursoSerializer
from rest_framework import viewsets

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1234',
            'nome': 'Maria'
        }
    return JsonResponse(estudante)

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

