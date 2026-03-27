def is_unique_id(user_id, ids):
    """Valida que el ID no esté repetido."""
    return user_id not in ids


def is_valid_name(name):
    """Valida que el nombre no esté vacío."""
    return name.strip() != ""


def is_valid_email(email, emails):
    """Valida formato básico y que no esté repetido."""
    return "@" in email and email not in emails


def is_valid_status(status):
    """Valida que el estado sea correcto."""
    return status in ["active", "inactive"]


def is_valid_age(age):
    """Valida que la edad sea un número válido y razonable."""
    
    if not isinstance(age, int):
        return False
    
    if age <= 0 or age > 120:
        return False
    
    return True