### 📂 Carga el dataset: Descarga el archivo Reto_01_Laptops_Dataset.csv y súbelo a tu Google Drive. Luego, carga el dataset en un DataFrame de Pandas.
### 📊 Calcular los estimados de locación: Calcula la media, mediana y moda de la columna price del dataset.
# 🔍 Análisis de resultados: Compara los resultados obtenidos e interpreta qué información nos proporcionan sobre la distribución de los precios de las laptops en el dataset.
# ✅ Desafío adicional: Si deseas practicar un poco más, puedes calcular lo mismo para la columna screen_size del dataset. ¿Qué información adicional puedes obtener de estos estimados de locación?

# Importar librerías
import pandas as pd

# Cargar el dataset
df = pd.read_csv('Reto_01_Laptops_Dataset.csv')

# Mostrar las primeras filas del dataset
print(df.head())

### Estadistica descriptuva de precios

# Calcular la media
promedio_price = df['price'].mean()
print(f'El promedio de los precios fue: {promedio_price}')

# Calcular la mediana
mediana_price = df['price'].median()
print(f'El valor central de los precios fue: {mediana_price}')

# Calcular la moda
moda_price = df['price'].mode()[0]
print(f'El precios más común  fue: {moda_price}')


### Estadistica descriptuva de screen_size

# Calcular la media
promedio_screen_size = df['screen_size'].mean()
print(f'El promedio de moda_screen_size fue: {promedio_screen_size}')

# Calcular la mediana
mediana_screen_size = df['screen_size'].median()
print(f'El valor central de moda_screen_size fue: {mediana_screen_size}')

# Calcular la moda
moda_screen_size = df['screen_size'].mode()[0]
print(f'El screen_size más común  fue: {moda_screen_size}')




