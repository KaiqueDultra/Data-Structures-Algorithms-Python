def fuel():
    tempo_gasto = float(input("Por favor, informe o tempo gasto na viagem: "))
    velocidade_media = float(input("Por favor, informe a velocidade média durante a viagem: "))

    distancia = tempo_gasto * velocidade_media
    litros_usados = distancia / 12

    print("A velocidade média foi de: ", velocidade_media)
    print("O tempo gasto na viagem foi de: ", tempo_gasto)
    print("A distancia  percorrida na viagem foi de: ", distancia)
    print("A quantidade de litros de gasolina utilizada na viagem foi de: ", round(litros_usados, 1))

if __name__ == '__main__':
    fuel()