"""Menú dinámico para ejecutar ejercicios desde la carpeta assets."""

import os
import importlib


def get_exercises():
    """Obtiene la lista de ejercicios disponibles en assets."""
    
    files = os.listdir("assets")
    
    exercises = [
        f.replace(".py", "")
        for f in files
        if f.startswith("exercise") and f.endswith(".py")
    ]
    
    return sorted(exercises)


def run_exercises_menu():
    """Muestra el menú dinámico de ejercicios."""
    
    while True:
        exercises = get_exercises()
        
        print("\n=== MENÚ DE EJERCICIOS ===")
        
        for i, ex in enumerate(exercises, start=1):
            print(f"{i}. {ex}")
        
        print("0. Volver")
        
        option = input("Seleccione una opción: ")
        
        if option == "0":
            break
        
        try:
            index = int(option) - 1
            exercise_name = exercises[index]
            run_exercise(exercise_name)
        
        except (ValueError, IndexError):
            print("Opción inválida")


def run_exercise(exercise_name):
    """Ejecuta un ejercicio dinámicamente."""
    
    try:
        module = importlib.import_module(f"assets.{exercise_name}")
        
        # Ejecuta función principal si existe
        if hasattr(module, "main"):
            module.main()
        
        else:
            print(f"El ejercicio {exercise_name} no tiene función main()")
    
    except Exception as e:
        print("Error ejecutando ejercicio:", e)

