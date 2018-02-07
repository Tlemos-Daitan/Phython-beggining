# python/biblioteca.py

def gera_nome_convite(convite):
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[ posicao_inicial:posicao_final]
  print (parte1, parte2)

def gera_nome_convite2():
  convite = 'Flavio Henrique Almeida'
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[posicao_inicial:posicao_final]
  print (parte1, parte2)

def gera_nome_convite3(convite):
  posicao_final = len(convite)
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[ posicao_inicial:posicao_final]
  return parte1 + ' ' + parte2  

