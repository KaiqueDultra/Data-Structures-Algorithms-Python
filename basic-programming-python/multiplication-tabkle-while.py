def tabuada():
    valor_tabuada = 3
    numero = 0
    
    while numero <= 10:
        print(f"{valor_tabuada} X {numero} = {valor_tabuada * numero}")
        numero += 1
    print("\n")
    
if __name__ == '__main__':
    tabuada()