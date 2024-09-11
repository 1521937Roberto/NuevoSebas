import matplotlib.pyplot as plt
# Crear los datos para la línea
x = [0, 10]
y = [0, 10]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar la línea
ax.plot(x, y, marker='o')  # Puedes añadir `marker='o'` para marcar los puntos extremos

# Ajustar los límites del gráfico para que se vean claramente las esquinas
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Añadir etiquetas para los ejes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Mostrar la cuadrícula (opcional)
ax.grid(True)

# Eliminar los recuadros y bordes del gráfico (spines)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Mantener las líneas de los ejes X e Y visibles
ax.spines['left'].set_linewidth(1)  # Ancho de la línea del eje Y
ax.spines['bottom'].set_linewidth(1)  # Ancho de la línea del eje X

# Ajustar el color de las líneas del eje (opcional)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

# Ajustar el fondo del gráfico a blanco
ax.set_facecolor('#ff3300')

# Mostrar el gráfico
plt.show()


