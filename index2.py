import matplotlib.pyplot as plt

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar una línea desde (0, 2) a (2, 4) con grosor de 2
ax.plot([0, 2], [2, 4], color='blue', linewidth=2, marker='o')  # Línea azul con grosor de 2

# Dibujar otra línea desde (2, 4) a (3, 0) con grosor de 3
ax.plot([2, 3], [4, 0], color='blue', linewidth=3, marker='o')  # Línea azul con grosor de 3

# Ajustar los límites del gráfico
ax.set_xlim(0, 3)
ax.set_ylim(0, 4)

# Configurar los ticks del eje x y el eje y para que solo muestren valores decimales
ax.set_xticks([0, 1.0, 2.0, 3.0])
ax.set_yticks([0, 1.0, 2.0, 3.0, 4.0])

# Ajustar el formato de los ticks para mostrar decimales
ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

# Ajustar el tamaño de las etiquetas de los ejes
ax.xaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje x
ax.yaxis.set_tick_params(labelsize=10)  # Tamaño de las etiquetas del eje y

# Ajustar el espaciado del gráfico
plt.subplots_adjust(left=0.15, right=0.75, top=1, bottom=0.25)

# Añadir etiquetas para los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Mostrar la cuadrícula (opcional)
ax.grid(True)

# Ajustar el fondo del gráfico a blanco
ax.set_facecolor('white')

# Mostrar el gráfico
plt.show()
