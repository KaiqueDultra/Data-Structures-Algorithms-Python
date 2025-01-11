import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)
    
    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True # Retorna True, pilha esta cheia
        else:
            return False # Retorna False, pilha não está cheia

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True # Retorna true se a pilha estiver vazia
        else:
            return False
    
    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia, não é possível inserir elementos.')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia, não é possível desempilhar.')
        else:
            self.__topo -= 1
    
    def ver_topo(self):
        if self.__topo != -1: # Se o topo for diferente de - 1, ou seja, se for diferente de pilha vazia
            return self.__valores[self.__topo]
        else:
            return -1

pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(6)
pilha.empilhar(8)
pilha.empilhar(9)
pilha.empilhar(20)
print(pilha.ver_topo())

pilha.desempilhar()
print(pilha.ver_topo())
