# Ejercicio 1: ordenar una lista de números ingresados por el usuario (Bubble sort)
# Instrucciones:

# Solicitar al usuario ingresar seis números separados por espacios.
# Usa el método de ordenación burbuja para organizarlos de menor a mayor.
# Muestra la lista ordenada.

numeros = input("Ingrese seies número separados por espacio").split()
for i in range (len(numeros)):
    numeros [i] = int(numeros[i])
n = len(numeros)
for i in range (n - 1):
    for j in range (n - 1 - i):
        if numeros [j] > numeros [j + 1]:
            numeros [j], numeros [j + 1] = numeros [j + 1], numeros [j]
print (f"La lista ordenada es: {numeros}")