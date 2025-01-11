# us - microsecond
# O(1000) ou O(n)
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

# ns - nanosecond
def lista2():
    return range(1000)