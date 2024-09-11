import matplotlib.pyplot as plt
import numpy as np

# Crear la figura y el eje
fig, ax = plt.subplots()

# Datos para las líneas
x1 = [1, 4]
y1 = [2, 6]

x2 = [4, 5]
y2 = [6, 3]

x3 = [5, 6]
y3 = [3, 6]

x4 = [6, 7]
y4 = [6, 3]

# Dibujar las líneas con bolas en los puntos finales
ax.plot(x1, y1, color='red', linestyle='--', linewidth=2, marker='o', markersize=8, label='Línea 1')  
ax.plot(x2, y2, color='red', linestyle='--', linewidth=2, marker='o', markersize=8, label='Línea 2')  
ax.plot(x3, y3, color='red', linestyle='--', linewidth=2, marker='o', markersize=8, label='Línea 3')  
ax.plot(x4, y4, color='red', linestyle='--', linewidth=2, marker='o', markersize=8, label='Línea 4')  

# Encontrar puntos de intersección manualmente
# Lista de puntos de intersección y sus colores correspondientes
intersection_points = [(1, 2), (4, 6), (5, 3), (6, 6), (7, 3)]
colors = ['blue','blue','blue','blue','blue']

# Añadir puntos de intersección con colores específicos
for (i, (xi, yi)) in enumerate(intersection_points):
    ax.plot(xi, yi, 'o', color=colors[i], markersize=10, label=f'Intersección {i+1}')  

# Ajustar los límites del gráfico
ax.set_xlim(1, 7)
ax.set_ylim(1, 7)

# Configurar los ticks del eje x y el eje y para que solo muestren valores decimales
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8])

# Ajustar el tamaño de las etiquetas de los ejes
ax.xaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje y

# Ajustar el espaciado del gráfico
plt.subplots_adjust(left=0.15, right=0.85, top=1.2, bottom=0.35)

# Añadir etiquetas para los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Mostrar la leyenda
ax.legend()

# Mostrar la cuadrícula (opcional)
ax.grid(True)

# Ajustar el fondo del gráfico a blanco
ax.set_facecolor('white')

# Mostrar el gráfico
plt.show()
