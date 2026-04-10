import requests
from colorama import Fore, Style, init

init(autoreset=True)

def fetch_users_from_api(users):
    """Trae usuarios desde API y los agrega."""
    
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        
        for item in data:
            
            new_user = {
                "id": max([u["id"] for u in users], default=0) + 1,
                "name": item["name"],
                "email": item["email"],
                "age": 30,  # valor fijo por ahora
                "status": "active"
            }
            
            users.append(new_user)
        
        print(f"{Fore.GREEN} Usuarios importados desde API")
    
    except Exception as e:
        print(f"{Fore.RED} Error:", e)