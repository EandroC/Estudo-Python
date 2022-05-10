
xPrimeiro = int(input("Digite o x do primeiro ponto cartesiano: "))
yPrimeiro = int(input("Digite o y do primeiro ponto cartesiano: "))
xSegundo = int(input("Digite o x do segundo ponto cartesiano: "))
ySegundo = int(input("Digite o y do segundo ponto cartesiano: "))

if xSegundo - xPrimeiro >= 10 or ySegundo - yPrimeiro >= 10:
 	print("longe")
else:
 	print("perto")
