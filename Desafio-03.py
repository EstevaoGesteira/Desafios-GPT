def frete():
    distancia = float(input("Digite a distância em km: "))
    expresso = input("Deseja entrega expressa? (s/n)")
    if expresso == "s":
        expresso = True
    if distancia < 0:
        print("Distância inválida!")
    if distancia > 0 and distancia <= 5:
        if expresso == True:
            print(f"Para a distância de: {distancia} km, O frete expresso é gratís!")
        else:
            print(f"Para a distância de: {distancia} km, O frete é grátis!")
    elif distancia > 5 and distancia <= 15:
        if expresso == True:
            print(f"Para a distância de: {distancia} km, O frete expresso custará R${(8 * 1.5)}")
        else:
            print(f"Para a distância de: {distancia} km, O frete custará R$8.00!")
    elif distancia > 15:
        if expresso == True:
            print(f"Para a distância de: {distancia} km, O frete expresso custará R${(15 * 1.5)}")
        else:
            print(f"Para a distância de: {distancia} km, O frete custará R$15.00")

frete()

