segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
restoSegundos = segundos % 86400
horas = restoSegundos // 3600
restoSegundos = restoSegundos % 3600
minutos = restoSegundos // 60
restoSegundos = restoSegundos % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e", restoSegundos,"segundos.")
