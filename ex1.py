#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("informe um numero"))
n2 = int(input("informe outro número"))
if n1 > n2:
    print(n1)
elif n2> n1:
    print(n2)
elif n1 == n2:
    print ("os numeros são iguais, refaça")
else:
    print("Informe um dado válido")