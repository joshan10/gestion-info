# abrir un archivo, capturar errores de apertura, contar lineas en else, cerrar el archivo en finally y mostrar un mensaje final.

def contar_lineas_archivo():
    try:
        nombre_archivo = input("Ingrese el nombre del archivo: ").strip() .split()
        archivo = open(nombre_archivo, 'r')
    
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    
    except IOError:
        print("Error: No se pudo abrir el archivo.")
    
    else:
        lineas = archivo.readlines()
        print(f"El número de líneas en el archivo es: {len(lineas)}")
    
    finally:
        try:
            archivo.close()
            print("Archivo cerrado correctamente.")
        except NameError:
            print("No se pudo cerrar el archivo porque no se abrió correctamente.")

contar_lineas_archivo()