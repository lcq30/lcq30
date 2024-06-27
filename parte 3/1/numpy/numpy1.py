import numpy as np
#genero numeros aleatorios
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(5, 4))
x3 = np.random.randint(10, size=(2, 4, 5))
print("Atributos de x1:")
print("Dimensiones (ndim):", x1.ndim)
print("Forma (shape):", x1.shape)
print("Tamaño (size):", x1.size)
print("Tipo de datos (dtype):", x1.dtype)
print("Tamaño de cada elemento (itemsize):", x1.itemsize)
print("Tamaño total en bytes (nbytes):", x1.nbytes)
print()
print("Atributos de x2:")
print("Dimensiones (ndim):", x2.ndim)
print("Forma (shape):", x2.shape)
print("Tamaño (size):", x2.size)
print("Tipo de datos (dtype):", x2.dtype)
print("Tamaño de cada elemento (itemsize):", x2.itemsize)
print("Tamaño total en bytes (nbytes):", x2.nbytes)
print()
print("Atributos de x3:")
print("Dimensiones (ndim):", x3.ndim)
print("Forma (shape):", x3.shape)
print("Tamaño (size):", x3.size)
print("Tipo de datos (dtype):", x3.dtype)
print("Tamaño de cada elemento (itemsize):", x3.itemsize)
print("Tamaño total en bytes (nbytes):", x3.nbytes)
