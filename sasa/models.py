from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Servicos (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class FormServicos (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.IntegerField()
    servico = models.ForeignKey(Servicos, on_delete= models.CASCADE)
    detalhes = models.TextField()
    data = models.DateField()
    aceita = models.BooleanField(default=None, null=True)

    def __str__(self):
        status = "Aceita" if self.aceita else "Negada" if self.aceita is False else "Pendente"
        return f"{self.nome} e {status}"
    
class UserBlog(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.cpf}"