from django.db import models

class Medico(models.Model):

    nome = models.CharField(max_length = 150)
    CRM = models.CharField(max_length = 150)


    def __str__(self):

        return self.nome