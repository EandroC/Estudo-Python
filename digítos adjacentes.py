numero = int(input("Digite um número inteiro: "))

condicional = True

while condicional:

    resto1 = numero%10
    novoNumero = numero//10
    resto2 = novoNumero%10
    
    if numero <= 10:
        print('não')
        condicional = False
        
    elif numero > 10 and resto1 == resto2:
        print('sim')
        condicional = False
        
    else:
        numero = numero//10
