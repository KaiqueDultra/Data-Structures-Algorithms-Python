import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def mostrar_no(self):
        print(self.valor)
        
class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None # Inidica a primeira cabeça da lista
        self.ultimo = None # Indica a ultima cabeça da lista
    
    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo
    
    def mostrar(self):
        if self.__lista_vazia():
            print('Lista vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
    
    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp