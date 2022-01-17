import random

#acá le estamos pidiendo que imprima numeros random del 1 al 100
print(random.randint(1,100))
#acá por ejemplo si incluye el 100 en el rango

# Para ejecutar el archivo se pone python + el nombre del archivo
# Las variables pueden ser con snake case o camel case

nombre_alex = "Naty"
calificación = 9.6
edad = 20
graduado = True
print( "Mi nombre es" + nombre_alex)
print(f"Mi calificación es {calificación}")
print(f"Mi edad es: {edad}")
print("Graduado: {}".format(graduado))
print("Calificación:" + str(calificación) )
print(type(graduado))
print(nombre_alex.upper())