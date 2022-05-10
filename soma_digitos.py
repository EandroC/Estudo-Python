numero = int(input("Digite um número inteiro: "))

resultado = 0

while (numero > 0):
	resto = numero % 10
	numero = numero // 10
	resultado = resultado + resto
	
print(resultado)
