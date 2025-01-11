'''
Funções Big-O
- Constant - O(n)
- Linear - O(n)
- Quadratic - O(n^2) - polynominal
- Combination

'''

# Constant - Função constante é aquela que tem um numero fixo, 
# um passo somente (ou dois passos) independente do numero de entradas.
lista = [1, 2, 3, 4, 5]
def constant(n):
    print(n[0])

#constant(lista)

# Linear O(n)
def linear(n):
    for i in n:
        print(n)

# linear(lista)

# Quadratic - O(n^2) - polynominal
def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
    print('-----')

# Combination
def combination(n):
    # O(1)
    print(n[0])
    
    # O(5) - Pois estamos executando o for 5 vezes, valor definido.
    for i in range(5):
        print('test, ', i)
    
    # O(n)    
    for i in n:
        print(i)
        
    # O(n)    
    for i in n:
        print(i)
    
    # O(3)    
    print('Python')
    print('Python')
    print('Python')
