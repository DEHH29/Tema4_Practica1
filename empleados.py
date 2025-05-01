# Importación de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creación de arreglos con numpy
productividad_semanal = np.array([75, 80, 90, 85, 70])
print("Productividad Semanal:", productividad_semanal)

# Operaciones con arreglos
print("Promedio de productividad:",
np.mean(productividad_semanal))
print("Productividad maxima:",
np.max(productividad_semanal))

# Lectura de archivos CSV con pandas
datos_empleados = pd.read_csv(r"C:\Users\DEHH29\Desktop\Program Logica y Funcional\TEC\Octavo\plyf\Tema4\empleados.csv",encoding='utf-8')
# Filtrar por departamento "Ventas" y hacer una copia del documento original
empleados_ventas = datos_empleados[datos_empleados["Departamento"] == "Ventas"].copy()
#Agregar columna de Bono
empleados_ventas['Bono'] = empleados_ventas['Salario'] * .10

print("\nDatos de empleados del departamento Ventas:\n", empleados_ventas)

# Visualización de datos con matplotlib
# Gráfica de barras de salario x empleado
plt.bar(datos_empleados['Nombre'],
datos_empleados['Salario'],
color='#90EE90')
plt.title('Salario por Empleado')
plt.xlabel('Nombre')
plt.ylabel('Salario')
plt.xticks(rotation=90) #Rota etiquetas del eje x
plt.grid(axis='y')
plt.tight_layout()      # Ajusta el espacio para que no se recorten etiquetas
plt.show()