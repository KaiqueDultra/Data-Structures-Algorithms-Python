import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor ordenado está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])
    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atingida.')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
            
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
            
        self.valores[posicao] = valor
        self.ultima_posicao += 1
        
    # O(n)
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.ultima_posicao > valor:
                return -1 # Não encontrou o valor no vetor, pois o número pesquisado é maior.
            if self.ultima_posicao == valor:
                return i
            if i == self.ultima_posicao: # Se o i estiver na ultima posicao, retorna -1, pois não encontrou o valor pesquisado.
                return -1
            
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            # Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou o valor
            elif limite_inferior > limite_superior:
                return -1
            # Dividir os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    # Se for superior
                    limite_superior = posicao_atual - 1
    
    # 0(n)
    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1
    

vetor = VetorOrdenado(10)
vetor.imprime()
vetor.insere(6)
vetor.insere(4)
vetor.insere(1)
vetor.imprime()