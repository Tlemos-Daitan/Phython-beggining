nomes = []
nome = input()

nomes.append(nome)
nomes

def cadastrar(nomes):
   print ('Digite o nome:')
   nome = input()
   nomes.append(nome)
   print (nomes)

nomes = []
cadastrar(nomes)