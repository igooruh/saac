from django.db import models
from hospital.models import Hospital
from medico.models import Medico
from paciente.models import Paciente
from comentario.models import Comentario
from avaliacao.models import Avaliacao

class Consultas(models.Model):

    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    hospital = models.ManyToManyField(Hospital)
    medico = models.ManyToManyField(Medico)
    paciente = models.ManyToManyField(Paciente)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)


    def __str__(self):

        return self.nome
