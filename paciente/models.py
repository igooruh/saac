from django.db import models

class Paciente(models.Model):

    nome = models.CharField(max_length = 150)
    CPF = models.CharField(max_length = 150)
    endereco = models.CharField(max_length = 150)
    CEP = models.CharField(max_length = 150)
    telefone = models.CharField(max_length = 150)

    def __str__(self):

        return self.nome