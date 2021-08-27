senha = int(input())

senha_valida = 2002

while senha != senha_valida:
    print("Senha Invalida")
    senha = int(input())

    if senha == senha_valida:
        print('Acesso Permitido')

        break