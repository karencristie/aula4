#modulo
#print(12%4 == 0)
n = (input("informe um valor numerico"))
if(int(n) %2 == 0):
    #print(f o {n} digitado é par)
    print("O número=> ", n, "digitado é par")
elif(int(n) % 2 == 1):
    #print(f'o {n} digitado é impar')
    print('O número =>' , n , 'digitado é impar')
else:
    print("Digite um valor numérico")