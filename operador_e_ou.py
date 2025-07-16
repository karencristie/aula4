dinheiro = False
senha = True

if dinheiro == True and senha == True:
    print('sacar')
elif dinheiro == True and senha == False:
    print("Senha Inválida!")
elif dinheiro == False and senha == True:
    print("saldo insuficiente")
elif dinheiro == False and senha == False:
    print("Dados incorretos")