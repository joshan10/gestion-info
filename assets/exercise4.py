#  Ejercicio 4: 
# Analiza el siguiente “código existente” y realiza un -> refactor <-, tener en cuenta los 
# problemas que se plantean al final.

# Código original (difícil de mantener)

# def calc(a, b, op):
#     if op == "s":
#         return a + b
#     elif op == "r":
#         return a - b
#     elif op == "m":
#         return a * b
#     elif op == "d":
#         if b == 0:
#              return "error"
#         return a / b
#     else:
#          return None

# Problemas:
# • Retorna "error" (string) o números → mezcla de tipos (confuso)
# • op con letras “mágicas”
# • No deja claro qué errores existen
# • Difícil testear los errores bien


try:    
    op = input("Ingrese la operación (suma, resta, multi, divi): ").strip().lower()
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    def calcular(num1, num2, op):
        ops = {
            "suma": lambda x, y: x + y,
            "resta": lambda x, y: x - y,
            "multi": lambda x, y: x * y,
            "divi": lambda x, y: x / y if y != 0 else ZeroDivisionError ("Error: División por cero no permitida") 
        }
    
        func = ops.get(op)
        return func(num1, num2) if func else "Error: Operación no válida"
    
    resultado = calcular(num1, num2, op)
    print(f"El resultado de la {op} es: {resultado}")

except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese números válidos.")

except ZeroDivisionError as e:
    print(e)


def main():
    print("Ejecutando", __name__)
