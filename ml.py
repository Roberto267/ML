import csv
import matplotlib.pyplot as plt

# Función para calcular la regresión lineal
def calcular_regresion_lineal(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(x_i ** 2 for x_i in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b

#Con esto va a leer datos del archivo CSV
experiencia = []
salario = []

with open('Salary_dataset.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la primera fila si contiene encabezados
    for row in reader:
        experiencia.append(float(row[1]))  # agarra los datos  de la tabla experiencia
        salario.append(float(row[2])) # agarra los datos  de la tabla salio

# Aqui va a Calcular la regresión lineal
a, b = calcular_regresion_lineal(experiencia, salario)

#Aqui Realiza predicciones
predicciones = [a * x + b for x in experiencia]

# Con esto va a Graficar los datos y la línea de regresión simple
plt.scatter(experiencia, salario, label='Datos reales', alpha=0.5)
plt.plot(experiencia, predicciones, color='red', linewidth=2, label='Línea de regresión lineal')
plt.xlabel('Experiencia')
plt.ylabel('Salario')
plt.legend()
plt.show()
