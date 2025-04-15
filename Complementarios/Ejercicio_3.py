print("--------------------------------------------------------------")
print("Complemento 3 : CAMBIOS DE PESOS ARGENTINOS A EUROS Y DÓLARES.")

EU = 1356
DO = 1285

print("Ingrese la cantidad de Pesos Argentinos : ")
P = float(input())

d = P/DO
e = P/EU

print("SALIDA : ")
print("--------------------------------------------------------------")
print("En", P, "Pesos hay", e,"Euros")
print("En", P,"Pesos hay", d,"Dólares")