from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12, unique=True)
    servico = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
