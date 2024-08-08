valor = int(input("Informe o valor: "))

# uso do if ternário

teste = "Sitação normal" if valor > 100 else "Situação: Pré-diabetes" if valor in range (100,125) else "Diabetes"

# Exibição
print(teste)
