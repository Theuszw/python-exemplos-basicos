# Entrada
print("Insira os valore.")
VProduto = float(input("Insira o valor do Produto: "))
PComissao = float(input("Insira a porcentagem da comissão: "))

# Calculo
Comissão = (VProduto * (PComissao / 100))

# Saída
print(f"A sua Comissão é de R${Comissão}")