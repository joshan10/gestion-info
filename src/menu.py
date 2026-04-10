from colorama import Fore, Style, init
from src.file import load_data, save_data
from src.service import new_register, list_records, search_record, update_record, delete_record
from src.integration import fetch_users_from_api
from assets.menu_exercise import run_exercises_menu 

# Inicializar colorama
init(autoreset=True)


def show_menu():
    """Muestra el menú principal."""
    
    print(Fore.CYAN + "\n=== MENU PRINCIPAL ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Importar usuarios desde API")
    print("7. Ejecutar ejercicios")
    print("8. salir")


def run_menu():
    """Ejecuta el menú interactivo."""
    
    users = load_data()
    
    while True:
        show_menu()
        
        option = input(Fore.YELLOW + "Seleccione una opción: ")
        
        # Validar que sea número
        try:
            option = int(option)
        except ValueError:
            print(Fore.RED + " Debe ingresar un número")
            continue
        
        # OPCIÓN 1
        if option == 1:
            name = input("Nombre: ")
            email = input("Correo: ")
            
            try:
                age = int(input("Edad: "))
            except ValueError:
                print(Fore.RED + " Edad inválida")
                continue
            
            status = input("Estado (active/inactive): ").lower()
            
            new_register(users, name, email, age, status)
            save_data(users)
        
        # OPCIÓN 2
        elif option == 2:
            list_records(users)
        
        # OPCIÓN 3
        elif option == 3:
            try:
                user_id = int(input("ID: "))
            except ValueError:
                print(Fore.RED + " ID inválido")
                continue
            
            user = search_record(users, user_id)
            if user:
                print(Fore.GREEN + f"\nUsuario encontrado:\n{user}")
        
        # OPCIÓN 4
        elif option == 4:
            try:
                user_id = int(input("ID: "))
            except ValueError:
                print(Fore.RED + " ID inválido")
                continue
            
            name = input("Nuevo nombre (opcional): ")
            email = input("Nuevo correo (opcional): ")
            age_input = input("Nueva edad (opcional): ")
            status = input("Nuevo estado (opcional): ").lower()
            
            age = None
            if age_input:
                try:
                    age = int(age_input)
                except ValueError:
                    print(Fore.RED + " Edad inválida")
                    continue
            
            update_record(
                users,
                user_id,
                name=name or None,
                email=email or None,
                age=age,
                status=status or None
            )
            save_data(users)
        
        # OPCIÓN 5
        elif option == 5:
            try:
                user_id = int(input("ID: "))
            except ValueError:
                print(Fore.RED + " ID inválido")
                continue
            
            delete_record(users, user_id)
            save_data(users)
        
        # OPCIÓN 6
        elif option == 6:
            fetch_users_from_api(users)
            save_data(users)
        
        # OPCIÓN 7
        elif option == 7:
            run_exercises_menu()
        
        # OPCIÓN 8
        elif option == 8:
            print(Fore.CYAN + "👋 Saliendo del sistema...")
            break
        
        else:
            print(Fore.RED + " Opción inválida")