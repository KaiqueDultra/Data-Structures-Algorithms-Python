'''
Notação Big-O
 - Como comparar dois algoritmos?
 - Comparação objetiva entre algoritmos.
 - Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
 - O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas

'''

# Função 1 - O(n)
def soma(n):
    soma = 0
    for i in range(n + 1):
        soma += 1
        
    return soma

# Função 2 
# 3 passos
# O(3)
def soma2(n):
    return (n * (n + 1)) / 2