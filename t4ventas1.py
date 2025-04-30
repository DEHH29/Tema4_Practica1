# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creación de arreglos con numpy
# Arreglo de ventas por semana
ventas_semana = np.array([150, 200, 170, 220, 300, 250,
190])
print("Ventas por semana:", ventas_semana)

# Operaciones con arreglos
print("Promedio de ventas:",
np.mean(ventas_semana))
print("Ventas máxima:",
np.max(ventas_semana))
print("Ventas mínima:",
np.min(ventas_semana))

# Lectura de archivos CSV con pandas
datos_ventas = pd.read_csv(r"C:\Users\DEHH29\Desktop\Program Logica y Funcional\TEC\Octavo\plyf\Tema4\ventas.csv",encoding='utf-8')
#Agregar columna de ventas totales
datos_ventas['Ventas Totales'] = datos_ventas['Unidades Vendidas'] * datos_ventas['Precio Unitario']
#Mostrar resultados
print("\nDatos de ventas:\n", datos_ventas)

#Lista de colores, uno por cada producto
colores = ['#7FFFD4', '#FFFFBA', '#BAFFC9', '#BAE1FF'] 

# Visualización de datos con matplotlib
# Gráfica de barras de Unidades Vendidas por Producto
plt.bar(datos_ventas['Producto'],
datos_ventas['Unidades Vendidas'],
color=colores)
plt.title('Unidades Vendidas por Producto')
plt.xlabel('Producto')
plt.ylabel('Unidades Vendidas')
plt.grid(axis='y')
plt.show()

# Gráfico de pastel
plt.pie(datos_ventas['Unidades Vendidas'],          # Valores numéricos
labels=datos_ventas['Producto'],                    # Etiquetas
autopct='%1.1f%%',                                  # Mostrar porcentajes con 1 decimal
startangle=90,                                      # Rotar inicio del gráfico
colors=colores                                      # Paleta de colores opcional
)
plt.title('Proporción de Unidades Vendidas por Producto')
plt.axis('equal')  # Hace el gráfico circular
plt.show()
