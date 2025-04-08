print("Ingrese número de partidos ganados")
PG = int(input())
print("Ingrese número de partidos perdidos")
PP = int(input())
print("Ingrese número de partidos empatados")
PE = int(input())

PPG = PG*3
PPP = PP*0
PPE = PE*1

PF = PPG + PPP + PPE

#Salida
print("\nSALIDA: ")
print("---------------------------------------------------------------")
print("Puntaje final", PF)