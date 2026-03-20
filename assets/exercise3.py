# #Ejercicio 3:
# #Crear un menú con: (1) dividir números,
# y mostrar primera línea, (3) salir.
# #Captura ValueError, ZeroDivisionError, FileNotFoundError y usa un except
# Exception final para no previstos.

def dividir_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def mostrar_primera_linea():
    try:
        nombre_archivo = input("Ingrese el nombre del archivo: ").strip()
        with open(nombre_archivo, 'r') as archivo:
            primera_linea = archivo.readline()
            print(f"La primera línea del archivo es: {primera_linea}")
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Dividir números")
        print("2. Mostrar primera línea de un archivo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            dividir_numeros()
        elif opcion == '2':
            mostrar_primera_linea()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()
