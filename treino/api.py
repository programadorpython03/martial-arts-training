from ninja import Router
from ninja.errors import HttpError
from .models import Alunos, AulasConcluidas
from .schemas import AlunosSchema, ProgressoAlunoSchema, AulaRealizadaSchema
from typing import List
from .graduacao import calculate_lesson_to_upgrade, order_belts
from datetime import date

treino_router = Router()

'''
GET: Listar alunos
POST: Criar aluno
PUT: Atualizar aluno
DELETE: Deletar aluno
'''

# Criar aluno
@treino_router.post("/", response={200: AlunosSchema})
def criar_aluno(request, aluno_schema: AlunosSchema):
    # Cadastrar aluno 
    if Alunos.objects.filter(email=aluno_schema.email).exists():
        raise HttpError(400, "Email já cadastrado")
    # Criar aluno a partir do schema usando a descompressão de dicionários
    aluno = Alunos.objects.create(**aluno_schema.dict())
    aluno.save()
    return aluno

# Listar alunos
@treino_router.get("/alunos/", response={200: List[AlunosSchema]})
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

# Progresso do aluno
@treino_router.get("/progresso_aluno/", response={200: ProgressoAlunoSchema})
def progresso_aluno(request, email_aluno: str):
    aluno = Alunos.objects.get(email=email_aluno)
    faixa_atual = aluno.get_faixa_display()
    belt_order = order_belts.get(faixa_atual, 0)
    aulas_necessarias_para_proxima_faixa = calculate_lesson_to_upgrade(belt_order)
    total_aulas_concluidas = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()
    aulas_restantes = aulas_necessarias_para_proxima_faixa - total_aulas_concluidas
    
    return {
        "email": aluno.email,
        "nome": aluno.nome,
        "faixa": faixa_atual,
        "total_aulas": total_aulas_concluidas,
        "aulas_necessarias_para_proxima_faixa": aulas_restantes
    }

# Aula realizada
@treino_router.post("/aula_realizada/", response={200: str})
def aula_realizada(request, aula_realizada: AulaRealizadaSchema):
    qtd = aula_realizada.dict()['qtd']
    email = aula_realizada.dict()['email_aluno']

    if qtd <= 0:
        raise HttpError(400, "Quantidade de aulas inválida")

    aluno = Alunos.objects.get(email=email)

    # for i in range(0, qtd):
    #     ac = AulasConcluidas(aluno=aluno, faixa_atual=aluno.faixa)
    #     ac.save()
    aulas = [
        AulasConcluidas(aluno=aluno, faixa_atual=aluno.faixa)
        for _ in range(qtd)
    ]
    AulasConcluidas.objects.bulk_create(aulas)

    return 200, f"Aula realizada com sucesso para o aluno {aluno.nome}"

# Atualizar aluno
@treino_router.put("/atualizar_aluno/{aluno_id}", response={200: AlunosSchema})
def atualizar_aluno(request, aluno_id: int, aluno_schema: AlunosSchema):
    aluno = Alunos.objects.get(id=aluno_id)
    idade = date.today().year - aluno_schema.data_nascimento.year

    if idade < 18 and aluno_schema.dict()['faixa'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, "Aluno menor de 18 anos não pode receber esta faixa.")
    
    for attr, value in aluno_schema.dict().items():
        if value:
            setattr(aluno, attr, value)
    aluno.save()
    return aluno

# Deletar aluno
@treino_router.delete("/deletar_aluno/{aluno_id}", response={200: str})
def deletar_aluno(request, aluno_id: int):
    aluno = Alunos.objects.get(id=aluno_id)
    aluno.delete()
    return f"Aluno {aluno.nome} deletado com sucesso"