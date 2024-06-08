import pandas as pd

# Datos proporcionados
notas = [1, 6, 8, 9, 10, 6, 5]
alumnos = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
apellidos = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

# Ajustar las notas sumando 1 punto y asegurando que no superen 10
notas_ajustadas = [min(n + 1, 10) for n in notas]

# Calcular las notas en texto según las condiciones dadas
notas_texto = ["suspendido" if n < 5 else
               "aprobado" if 5 <= n <= 6 else
               "bien" if 6 < n < 7 else
               "notable" if 7 <= n < 9 else
               "Excelente" if n >= 9 and n < 10 else
               "matrícula de honor" for n in notas_ajustadas]

# Calcular la diferencia y el porcentaje de diferencia respecto a la mediana
mediana = pd.Series(notas_ajustadas).median()
diferencia = [n - mediana for n in notas_ajustadas]
porcentaje_diferencia = [(n - mediana) / mediana * 100 for n in notas_ajustadas]

# Crear el DataFrame con los datos obtenidos
df = pd.DataFrame({
    'Nombre y Apellidos': [f"{a} {apellidos[i]}" for i, a in enumerate(alumnos)],
    'Nota': notas_ajustadas,
    'Nota en Texto': notas_texto,
    'Diferencia respecto a la mediana': diferencia,
    'Diferencia en Porcentaje respecto a la mediana': porcentaje_diferencia
})

# Guarda el DataFrame en un archivo CSV
df.to_csv('notas_alumnos.csv', index=False)

# Muestra el DataFrame
print(df)
