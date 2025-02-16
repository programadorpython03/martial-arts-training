from django.db import models

# Create your models here.
FAIXA_CHOICES = [
  ('B', 'Branca'),
  ('A', 'Azul'),
  ('R', 'Roxa'),
  ('M', 'Marrom'),
  ('P', 'Preta')
]

class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    faixa = models.CharField(max_length=1, choices=FAIXA_CHOICES, default='B')
    data_nascimento = models.DateField(null=True, blank=True  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class AulasConcluidas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    faixa_atual = models.CharField(max_length=1, choices=FAIXA_CHOICES, default='B')
    data = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.aluno.nome}"