from django.db import models
from django.urls import reverse


class Genero(models.Model):
    nome = models.CharField(max_length=200, help_text="Digite um gênero de jogo")

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    desenvolvedora =  models.ForeignKey('Desenvolvedora', on_delete=models.SET_NULL, null=True)
    sinopse = models.TextField(max_length=1000, help_text="Digite a sinopse do jogo.")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('jogo-detalhe', args=[str(self.id)])

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

    class Meta: 
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('desenvolvedora-detalhe', args = [str(self.id)])

    def __str__(self):
        return f'{self.nome}'

