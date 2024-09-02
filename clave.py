import secrets

# Genera una clave secreta de 50 caracteres
secret_key = secrets.token_urlsafe(50)
print(secret_key)
