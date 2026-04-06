from file import load_data, save_data
from service import new_register, list_records, search_record, update_record, delete_record


def menu():
    users = load_data()
    
    while True:
        print("\n--- MENU ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Salir")
        
        option = input("Seleccione: ")
        
        if option == "1":
            name = input("Nombre: ")
            email = input("Correo: ")
            age = int(input("Edad: "))
            status = input("Estado (active/inactive): ").lower()
            
            new_register(users, name, email, age, status)
            save_data(users)
        
        elif option == "2":
            list_records(users)
        
        elif option == "3":
            user_id = int(input("ID: "))
            user = search_record(users, user_id)
            if user:
                print(user)
        
        elif option == "4":
            user_id = int(input("ID: "))
            name = input("Nuevo nombre (opcional): ")
            email = input("Nuevo correo (opcional): ")
            age_input = input("Nueva edad (opcional): ")
            status = input("Nuevo estado (opcional): ").lower()
            
            age = int(age_input) if age_input else None
            
            update_record(users, user_id, name or None, email or None, age, status or None)
            save_data(users)
        
        elif option == "5":
            user_id = int(input("ID: "))
            delete_record(users, user_id)
            save_data(users)
        
        elif option == "6":
            break
        
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()