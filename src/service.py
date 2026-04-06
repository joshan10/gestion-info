from validate import is_valid_name, is_valid_email, is_valid_status, is_valid_age
from file import load_data, save_data

# Datos cargados
users = load_data()

# Sets para control de duplicados
ids = {1, 2}
emails = {"juan@gmail.com", "ana@gmail.com"}

def generate_id():
    """Genera un ID único automáticamente."""
    if not ids:
        return 1
    return max(ids) + 1


def new_register(users, name, email, age, status):
    """Crea un nuevo usuario con ID automático."""
    
    user_id = generate_id()
    
    if not is_valid_name(name):
        print("ERROR: Nombre inválido")
        return
    
    if not is_valid_email(email, emails):
        print("ERROR: Correo inválido o duplicado")
        return
    
    if not is_valid_age(age):
        print("ERROR: Edad inválida")
        return
    
    if not is_valid_status(status):
        print("ERROR: Estado inválido")
        return
    
    user = {
        "id": user_id,
        "name": name,
        "email": email,
        "age": age,
        "status": status
    }
    
    users.append(user)
    ids.add(user_id)
    emails.add(email)
    
    print(f" Usuario creado con ID: {user_id}")

def list_records(users):
    """Muestra todos los usuarios registrados."""
    
    if not users:
        print("No hay usuarios")
        return
    
    print("\n--- LISTA DE USUARIOS ---")
    for u in users:
        print(f"ID: {u['id']} | Name: {u['name']} | Email: {u['email']} | Age: {u['age']} | Status: {u['status']}")
    
    active_users = [u for u in users if u["status"] == "active"]
    
    print(f"\nUsuarios activos: {len(active_users)}")


def search_record(users, user_id):
    """Busca un usuario por ID usando list comprehension."""
    result = [u for u in users if u["id"] == user_id]

    if not result:
        print("Usuario no encontrado")
        return None
    
    return result[0]

def update_record(users, user_id, name=None, email=None, age=None, status=None):
    """Actualiza un usuario."""
    
    user = search_record(users, user_id)
    
    if user is None:
        return
    
    if name:
        if is_valid_name(name):
            user["name"] = name
        else:
            print("Nombre inválido")
    
    if email:
        if is_valid_email(email, [u["email"] for u in users if u["id"] != user_id]):
            user["email"] = email
        else:
            print("Correo inválido o duplicado")
    
    if age is not None:
        if is_valid_age(age):
            user["age"] = age
        else:
            print("Edad inválida")
    
    if status:
        if is_valid_status(status):
            user["status"] = status
        else:
            print("Estado inválido")
    
    print("Usuario actualizado")


def delete_record(users, user_id):
    """Elimina un usuario."""
    
    user = search_record(users, user_id)
    
    if user is None:
        return
    
    users.remove(user)
    print("Usuario eliminado")