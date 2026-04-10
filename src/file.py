import json

FILE_PATCH = "data/records.json"

def load_data() -> list:
    """carga todos los datos desde un archivo json"""

    try:
        with open(FILE_PATCH, "r") as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Archivo JSON dañado")
        return []
    

def save_data(data):
    """Guarda los datos en un archivo JSON."""

    try:
        with open(FILE_PATCH, "w") as file:
            json.dump(data, file, indent=4 )

    except Exception as e:
        print(f"Error al guardar los datos {e}")
