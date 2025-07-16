try:
    numero = int(input('Digite um número'))
    #print("Deu bom...")
    if(numero % 2 == 0):
        print("o numero é par")
    elif(numero % 2 != 0):
        print("o número é ímpar")
    else:
        print("Número Inválido")
except:
    print("Deu ruim...")

    #vai executar um bloco ou o outro para tratamento