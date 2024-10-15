import numpy as np

# Función para interpolación de Newton
def newton_interpolation(x, y, value):
    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x[i + j] - x[i])

    # Calcular el valor interpolado
    result = divided_diff[0, 0]
    term = 1
    for i in range(1, n):
        term *= (value - x[i - 1])
        result += divided_diff[0, i] * term

    return result

# Función para interpolación de Lagrange
def lagrange_interpolation(x, y, value):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    return result

# Datos de población (año vs población en millones, ejemplo de La Paz)
x = [1990, 2000, 2010, 2020]  # Años
y = [3022566, 3500000, 3800000, 4000000]  # Población (estimada)

# Año para interpolar
year_to_interpolate = 2024

# Resultados de la interpolación
newton_result = newton_interpolation(x, y, year_to_interpolate)
lagrange_result = lagrange_interpolation(x, y, year_to_interpolate)

# Mostrar los resultados
print(f'Interpolación de Newton para el año {year_to_interpolate}: {newton_result}')
print(f'Interpolación de Lagrange para el año {year_to_interpolate}: {lagrange_result}')
