# Reset contador e limites de tentativas
i = 1
while i <= 3:

    user = input("Informa o usuario: ")
    senha = input("Informe a senha: ")

    # Checagem
    if user != "Gisele" and senha != "123":
        i += 1
        print("Usuário ou Senha incorretos!")
        print(" ")
    else:
        print(" ")
        print("Bem vindo, {user}!")
        break

else:
    print(f"Você excedeu todas as: {i-1} tentativas!!")