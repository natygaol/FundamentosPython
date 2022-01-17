#
numeros = [10, 20, 30, 40, 50]

i = 0
while i < len(numeros):
    print( numeros[i])
    i += 1
#else: <- se puede poner aveces pero no es comun
#else: print("se termino el ciclo")

#primer parámetro es el índice, el segundo el límite y el tercero de cuanto en cuanto avanza
#acá la x es el índice , si quiero el nùmero: numero[x]
for x in range (0, len(numeros), 2):
  print(x)

for y in range(1, 11):
  print(y)


# se utiliza cuando no necesitas el índice, porque el elemento es el valor del array.
for elemento in numeros:
  print(numeros)
  
  
  estudiante = {
  "nombre" : "Naty",
  "apellido" : "García",
  "edad" : 33
}
  
for key in estudiante:
  print(key)
  print(estudiante[key])