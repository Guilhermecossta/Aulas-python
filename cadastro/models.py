from django.db import models

# Create your models here.
class Estudante(models.model):
    nome = models.CharField(max_length=100, null = False, blank = False)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=30,blank = False)
    data_nascimento = models.CharField()
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Curso(models.model):
    NIVEL = (
        ('B', "basico"),
        ('I', "intermediario"),
        ('A', "avançado"),
    )
    codigo = models.CharField(max_length=14)
    descricao = models.CharField(null=False, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default="B")

    def __str__(self):
        return self.codigo


    
