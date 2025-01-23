# Ejercicio 3: Ordenar lista de palabras alfabeticamente (Insertion Sort)
# Instrucciones:
# Solicictar al usuario que ingrese 5 palabras separadas por espacios.
# Ordenar las palabras en orden alfabético utilizando el metodo de inserción.
# Muestra la lista ordenada.

palabras = input ("Ingrese 5 palabras separados por espacio: ").split()
for i in range(1, len(palabras)):
     clave = palabras [i]
     j = i - 1
     while j >= 0 and clave < palabras [j]:
          palabras [j + 1] = palabras [j]
     palabras [j + 1] = clave
print (f"Palabras ordenadas alfabeticamente: {palabras}")