# Complejidad algoritmica y metodos de ordenación.
# (Bubble Sort e insertion sort)

# Cuando trabajmos con algotrimos es fundamental evaluar que tan eficientes son en terminos de ejecución y uso de 
# memoria. Esta eficiencia se mide medieante la complehidad algoritmica. Esto nos ayuda a estimar el comportamiento 
# algortimo cuando el tamaño de los datos crece

# La complejidad algoritmica mide los recursos que necesita un algoritmo para ejecutarse. en este caso se mide en terminos de:
# Tiempo d ejecucipon complejidad temporal:
# Cuanto tiepo toma ehjecutar al algoritmo en funcipon de la cantidad de los datos de enetrasa (n), se suele expresar en big O O(n),
# O (n2), O (Long n).

# Uso de memoria o comnplejidad espacial):
# Cuanta memoria adicional requiere el algoritmo para ejecutarse.
# Tambien se expresa con big O

# Notacion de Big O
# describir como crece el tiempo de ejecuciomn de un algoritmo en en relacion a su tamaño de entrada . 
# algunos de los ordenes de complejidad mas comunes son:

# como ordenar...

# Es el proceso de organizar elementos en un orden especifico (asendentes y descendestes). Existen multiples.
# algoritmos de ordenación, cada uno con sus ventajas  y sus desventajas, sobre todo en terminos de eficiencia.

# Ordenación por burbuja o bubble sort.
# Este algoritmo compara elementos adyecentes y los intercambia si estan en orden incorrecto, esto se repite
# hasta que no necesiten más intercambios.

# En el mejor de los casos es lineal. En el peor, cuadratico y especialmente hablando es constante.


#  numeros = [5, 3, 8, 4, 2]
#  n = len(numeros)

#  for i in range (n - 1):
#     for j in range (n - 1 - i):
#          if numeros [j] > numeros [j + 1]:
#              temp = numeros [j]
#              numeros [j] = numeros [j + 1]
#              numeros [j + 1] = temp
#  print (f"lista ordenada con bbuble sort: {numeros}")

# Ventajas:
# Facíl de entender y de implementar.
# Funciona bien con listas pequeñas.

# Desventajas:
# Ineficiente para listas grandes.
# Aveces realiza muchas comparaciones que son innecesarias.  

# Metodo de ordenación por inserción:
# Construyo una lista ordenada de manera incremental,insertando cada elemento en la posición correcta
# respecto a los ya ordenados 
# En el mejor de los casos es lineal.
# En el peor de los casos es cuadratico.
# Espacialmente hablando es constante.


# num = [7, 3, 5, 2, 6]
# n = len(num)

# for i in range (1, n):
#    clave = num[i]
#    j = i - 1
#    while j >= 0 and num [j] > clave:
#       num [j + 1] = num [j]
#       j -= 1
#    num [j + 1] = clave
# print (f"Lista ordenada con inserción: {num}")