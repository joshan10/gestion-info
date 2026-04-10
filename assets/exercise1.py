# # leer enteros separados por comas, calcular el promedio y manejar errores de conversion. corrige ademas el calculo logico del promedio.

def calcular_promedio():
     try:
         numeros_str = input("Ingrese números enteros separados por comas: ")
         numeros = [int(num.strip()) for num in numeros_str.split(",")]
       
         if len(numeros) == 0:
             raise RuntimeError("No se ingresaron números.")
       
         promedio = sum(numeros) / len(numeros)
         print(f"El promedio es: {promedio}")
   
     except RuntimeError as e:
         print(f"Error: {e}")

def main():
    calcular_promedio()
    print("Ejecutando", __name__)