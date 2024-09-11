import matplotlib.pyplot as plt
import numpy as np

# Datos para las curvas
x = np.linspace(0.1, 10, 100)
y1 = x ** 2
y2 = x ** 2.4
y3 = np.log(x)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 5))  # Cambiar tamaño de la figura para hacerla más ovalada

# Graficar las curvas con los estilos especificados
ax.plot(x, y1, 'o-', label=r'$y=x^2$', markersize=5)  # Primera línea: triángulos
ax.plot(x, y2, 's-', label=r'$y=x^{2.4}$', markersize=3)  # Segunda línea: círculos pequeños
ax.plot(x, y3, '--', label=r'$y=\log{x}$')  # Tercera línea: guiones

# Establecer los límites de los ejes
ax.set_xlim(0, 10)
ax.set_ylim(-5, 100)

# Personalización del gráfico
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Etiquetas de los ejes
ax.set_xlabel(r'$x$', loc='right')
ax.set_ylabel(r'$y$', loc='top')

# Mostrar leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
