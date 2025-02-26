from rest_framework import serializers
from tarefa.models import Estudantes
from cadastro.serializers import EstudanteSerializer,CursoSerializer
from rest_framework import viewsets


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all_from escola.models import Estudante,Curso'
