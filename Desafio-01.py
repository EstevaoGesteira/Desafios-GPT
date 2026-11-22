nome_produto = input("Digite o nome do produto: ")
unidade = int(input("Digite a quantidade comprada: "))
preco = float(input("Digite o valor do produto: "))

print()
total = unidade * preco
print(f"Produto: {nome_produto}")
print(f"Quantidade comprada: {unidade}")
print(f"Preço unitário: R${preco:.2f}")
print(f"Valor total da compra: R${total:.2f}")