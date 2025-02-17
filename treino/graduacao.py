import math

# def calcular_graduacao(faixa_atual, aulas_concluidas):
#     if faixa_atual == 'B':
#         return math.ceil(aulas_concluidas / 10)
#     elif faixa_atual == 'A':
#         return math.ceil(aulas_concluidas / 20)

# Cria um dicionário com as faixas e o número de aulas para cada faixa
order_belts ={ "Branca": 0, "Azul": 1, "Roxa": 2, "Marrom": 3, "Preta": 4 }

def calculate_lesson_to_upgrade(n):
  d = 1.47
  k = 30 / math.log(d)
  aulas = k * math.log(n + d)

  return round(aulas)
