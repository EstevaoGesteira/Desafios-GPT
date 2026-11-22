def media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    med = (n1+n2+n3)/3
    print()
    if med >= 6:
        print(f"Sua media foi {med}")
        print(f"Você foi aprovado!")
    else:
        print(f"Sua media foi {med}")
        print(f"Você foi reprovado!")

print()
media()

