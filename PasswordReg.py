import re
 
def password_valida(password):
    # Controlla la lunghezza della password (almeno 8 caratteri)
    if len(password) < 8:
        return False
    # Controlla se la password contiene almeno una lettera minuscola
    if not re.search(r'[a-z]', password):
        return False
    # Controlla se la password contiene almeno una lettera maiuscola
    if not re.search(r'[A-Z]', password):
        return False
    # Controlla se la password contiene almeno un numero
    if not re.search(r'\d', password):
        return False
    # Controlla se la password contiene almeno un carattere speciale
    if not re.search(r'[!@#$%^&£*]', password):
        return False
    return True
 
# Esempi di password da testare
passwords = [
    "Password123!",
    "abcDEF456",
    "12345678",
    "!@#$%^&*",
    "SofnqDfn45@",
    "Abcdefgh"
]
 
# Verifica se le password sono valide o meno
for password in passwords:
    if password_valida(password):
        print(f"{password}: Password valida")
    else:
        print(f"{password}: Password non valida")
