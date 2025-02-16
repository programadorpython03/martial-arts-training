from ninja import ModelSchema, Schema
from .models import Alunos
from typing import Optional

# Schema para o aluno
class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']

# Schema para o progresso do aluno
class ProgressoAlunoSchema(Schema):
    class Meta:
        email: str
        nome: str
        faixa: str
        total_aulas: int
        aulas_necessarias_para_proxima_faixa: int

class AulaRealizadaSchema(Schema):
    class Meta:
        qtd: Optional[int] = 1
        email_aluno: str
