'''
Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
'''

import numpy as np

def soma():
    soma = 0
    matriz = np.array([[3, 4, 1],
                       [3, 1, 5]])
    
    # .shape retorna o valor da linha e da coluna. (2, 3), posição 0 = quantidade de linhas (2)
    # e posição 1 = quantidade de colunas (3)
    # print(matriz.shape) 
    
    for i in range(matriz.shape[0]): # For para acessar as linhas da matriz
        for j in range(matriz.shape[1]): # For para acessar as colunas da matriz
            soma += matriz[i][j]
    print(f"A soma de todos os elementos da matriz é de: {soma}")

if __name__ == '__main__':
    soma()