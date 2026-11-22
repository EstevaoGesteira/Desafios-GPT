vendas =[]

while True:
    venda = float(input("Digite o valor da venda (digite 0 para sair): "))
    if venda == 0:
        print("Saiu!")
        break
    elif venda < 0:
        print(f"Valor inválido!")
    else:
        vendas.append(venda)

if len(vendas) > 0 :
    print(f"\nVendas registradas: {len(vendas)}")
    print(f"Total vendido: R${sum(vendas)}")
    print(f"Média das vendas: {sum(vendas)/len(vendas)}")
    print(f"Maior venda: {max(vendas)}")
    print(f"Menor venda: {min(vendas)}")
else:
    print("\nNenhuma venda válida foi registrada.")
