import matplotlib.pyplot as plt
import pandas as pd

# Fechas (ejemplo de datos de fechas)
fechas = pd.date_range('2016-10-03', periods=5)

# Valores que me proporcionaste
valores = [772.5, 776.5, 776.5, 776.75, 775.0]

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos con una línea roja y puntos marcados
ax.plot(fechas, valores, 'o-', color='red')

# Establecer los límites en el eje y (desde 772.5 a 777.0)
ax.set_ylim(772.5, 777.0)

# Formatear el gráfico
ax.set_xlabel('Fecha')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Valores a lo Largo del Tiempo')

# Rotar las etiquetas del eje x para que se vean mejor
plt.xticks(rotation=45)

# Mostrar la gráfica
plt.show()
