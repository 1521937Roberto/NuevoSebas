import matplotlib.pyplot as plt

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar una línea desde (0, 2) a (2, 4) con grosor de 2
ax.plot([10, 20], [20, 40], color='blue', linewidth=2, marker='o')  # Línea azul con grosor de 2

# Dibujar otra línea desde (2, 4) a (3, 0) con grosor de 3
ax.plot([30,20], [10,40], color='blue', linewidth=2, marker='o')  # Línea azul con grosor de 3

# Dibujar otra línea desde (2, 4) a (3, 0) con grosor de 3
ax.plot([10,20], [40,10], color='green', linewidth=2, marker='o')  # Línea azul con grosor de 3

# Dibujar otra línea desde (2, 4) a (3, 0) con grosor de 3
ax.plot([20,30], [10,30], color='green', linewidth=2, marker='o')  

# Ajustar los límites del gráfico
ax.set_xlim(10, 30)
ax.set_ylim(10, 40)

# Configurar los ticks del eje x y el eje y para que solo muestren valores decimales
ax.set_xticks([10, 15, 20, 25, 30])
ax.set_yticks([10, 15, 20, 25, 30, 35, 40])


# Ajustar el tamaño de las etiquetas de los ejes
ax.xaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje y

# Añadir etiquetas para los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Mostrar la cuadrícula (opcional)
ax.grid(True)

# Ajustar el fondo del gráfico a blanco
ax.set_facecolor('white')

# Mostrar el gráfico
plt.show()
