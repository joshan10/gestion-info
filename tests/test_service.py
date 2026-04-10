import sys
import os

# Agrega la raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service import generate_id, new_register, delete_record, search_record


def test_generate_id():
    """Verifica que el ID generado sea el siguiente al mayor existente."""
    
    users = [{"id": 1}, {"id": 2}, {"id": 3}]
    
    new_id = generate_id(users)
    
    assert new_id == 4


def test_new_register():
    """Comprueba que se pueda crear un nuevo usuario correctamente."""
    users = []
    
    # limpiar emails antes del test
    from src.service import emails
    emails.clear()
    
    new_register(users, "Juan", "juan@gmail.com", 20, "active")
    
    assert len(users) == 1

def test_search_record():
    """Comprueba que se pueda encontrar un usuario por ID."""
    
    users = [{"id": 1, "name": "Juan"}]
    
    user = search_record(users, 1)
    
    assert user is not None
    assert user["name"] == "Juan"


def test_delete_record():
    """Valida que un usuario sea eliminado correctamente."""
    
    users = [{"id": 1, "name": "Juan"}]
    
    delete_record(users, 1)
    
    # La lista debe quedar vacía después de eliminar
    assert len(users) == 0