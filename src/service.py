from validate import is_valid_name, is_valid_email, is_valid_status, is_valid_age

# Datos en memoria (2 usuarios iniciales)
users = [
    {"id": 1, "name": "Juan", "email": "juan@gmail.com", "age": 20, "status": "active"},
    {"id": 2, "name": "Ana", "email": "ana@gmail.com", "age": 25, "status": "inactive"}
]

# Sets para control de duplicados
ids = {1, 2}
emails = {"juan@gmail.com", "ana@gmail.com"}

def generate_id():
    """Genera un ID único automáticamente."""
    if not ids:
        return 1
    return max(ids) + 1


def create_user(name, email, age, status):
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

def list_users():
    """Muestra todos los usuarios registrados."""
    
    if not users:
        print("No hay usuarios")
        return
    
    print("\n--- LISTA DE USUARIOS ---")
    for u in users:
        print(f"ID: {u['id']} | Name: {u['name']} | Email: {u['email']} | Age: {u['age']} | Status: {u['status']}")