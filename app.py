
# -*- coding: UTF-8 -*-


def cadastrar(nomes):
    print ("Digite: o nome:")
    nome = input()
    nomes.append(nome)
    
def listar(nomes):
    print ("Listando nomes:")
    for nome in nomes:
        print (nome)

def remover(nomes):
    print ("Qual nome você gostaria de remover?")
    nome = input()
    nomes.remove(nome)

def alterar(nomes):
    print ("Qual nome vc gostaria de alterar?")


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print ("Digite: 1 para cadastrar, 2 para listar, 3 para remover e 0 para terminar")
        escolha = input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
menu()