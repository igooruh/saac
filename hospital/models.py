from django.db import models

class Hospital(models.Model):

    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    cnpj = models.CharField(max_length = 150)
    local = models.CharField(max_length = 200)
    telefone = models.CharField(max_length = 200)



    def __str__(self):

        return self.nome