import datetime

from django.db import models
from django.urls import reverse


class Genero(models.Model):
    nome = models.CharField(max_length=200, help_text="Digite um gênero de jogo")

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    desenvolvedora =  models.ForeignKey('Desenvolvedora', on_delete=models.SET_NULL, null=True)
    lancamento = models.DateField(null=True, blank=True)
    sinopse = models.TextField(max_length=1000, help_text="Digite a sinopse do jogo.")
    review = models.TextField(max_length=4000, help_text="Digite a review do jogo.", default="")
    plataforma = models.ForeignKey('Plataforma', on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to='images', default="Capa do jogo.")
    data_publicacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('jogo-detail', args=[str(self.id)])

    class Meta:
        ordering = ['titulo']

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)    

    def get_absolute_url(self):
        return reverse('desenvolvedora-detalhe', args = [str(self.id)])

    def __str__(self):
        return f'{self.nome}'

    class Meta: 
        ordering = ['nome']

class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    class Meta: 
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('plataforma-detalhe', args = [str(self.id)])

    def __str__(self):
        return f'{self.nome}'
