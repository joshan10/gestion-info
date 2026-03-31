from file import load_data, save_data
from service import create_user, list_users


def menu():
    """Menú principal del sistema."""
    
    while True:
        print("\n--- MENU ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Salir")

        users = load_data()
        option = input("Seleccione una opción: ")
        
        if option == "1":
            try:
                name = input("Nombre: ")
                email = input("Correo: ")
                age = int(input("Edad: "))
                status = input("Estado (active/inactive): ").lower()
                
                create_user(users, name, email, age, status)
                save_data(users)
            
            except ValueError:
                print("La edad debe ser un número")
        
        elif option == "2":
            list_users(users)
        
        elif option == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()