                                            
#Estudo Phyton

- Variáveis

    >>> convite = 'Romulo Henrique'
    >>> parte1 = convite[0:4]
    >>> parte2 = convite[11:15]

    >>> print(parte1, parte2)


    >>> convite = 'Flavio Henrique Almeida'
    >>> tamanho = len(convite)
    >>> parte1 = convite[0:4]
    >>> parte2 = convite[tamanho-4:tamanho]
    
    >>> print(parte1, parte2)

- Funções (No arquivo: biblioteca.py)

   def gera_nome_convite():
     convite = 'Flavio Henrique Almeida'
     posicao_final = len(convite)
     posicao_inicial = posicao_final - 4
     parte1 = convite[0:4]
     parte2 = convite[posicao_inicial:posicao_final]
     print (parte1, parte2)

   def gera_nome_convite2(convite):
     convite = 'Flavio Henrique Almeida'
     posicao_final = len(convite)
     posicao_inicial = posicao_final - 4
     parte1 = convite[0:4]
     parte2 = convite[ posicao_inicial:posicao_final]
     print (parte1, parte2)

