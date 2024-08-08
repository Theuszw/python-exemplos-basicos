# Matheus Ferreira

comida = int(input("Indique a opção desejada: "))

# Seleção de opções
match comida:
    case 1:
        print("Bolo. ")
    case 2:
        print("Pizza. ")
    case 3:
        print("Refrigerante. ")
    case _:
        print("Opção inválida!")