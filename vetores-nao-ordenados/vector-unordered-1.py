import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        # Criando um atributo Capacidade
        self.capacidade = capacidade
        # self.ultima_posicao = -1, por exemplo, se temos um vetor com 10 
        # posiçoes, e estamos usando apenas 5 posições, essa variavel serve  
        # como um ponteiro que vai armazenar aonde esta o ultimo elemento.
        self.ultima_posicao = -1
        # Criando o vetor vazio, pois a capacidade do vetor dependera da quantidade
        # informada pelo input.
        self.valores = np.empty(self.capacidade, dtype=int)
    # O(n)    
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")
        else:
            # Percorrendo todos os elementos do vetor
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])
    # O(1)            
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    # O(n)
    def pesquisar(self, valor):
        # Pesquisa Linear, verificando posição por posição, percorrer o vetor inteiro
        # até que ele encontre o valor pesquisado
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    # O(n)
    def excluir(self, valor):
        # Encontrar se o valor existe no vetor
        posicao = self.pesquisar(valor)
        if posicao == -1: # Se for igual a -1, o elemento nao existe
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1] # Posicao de exclusao recebe a proxima posicao
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

vetor.imprime()
vetor.excluir(5)
print('--------------')
vetor.imprime()
#print(vetor.pesquisar(10))
