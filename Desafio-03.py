def frete():
    distancia = float(input("Digite a distância em km: "))
    expresso = input("Deseja entrega expressa? (s/n)")
    if expresso == "s":
        expresso = True
    if distancia <= 5:
        if expresso == True:
            print(f"Para a distâmcia de: {distancia} km, O Frete expresso é gratís!")
        else:
            print(f"Para a distâmcia de: {distancia} km, O Frete é grátis!")
    elif distancia > 5 and distancia <= 15:
        if expresso == True:
            print(f"Para a distâmcia de: {distancia} km, O frete expresso custára R${(8 * 1.5)}")
        else:
            print(f"Para a distâmcia de: {distancia} km, O frete custára R$8.00!")
    else:
        if expresso == True:
            print(f"Para a distâmcia de: {distancia} km, O frete expresso custará R${(15 * 1.5)}")
        else:
            print(f"Para a distâmcia de: {distancia} km, O frete custará R$15.00")

frete()

