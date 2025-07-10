from cryptography.fernet import Fernet

_key = Fernet.generate_key()
fernet = Fernet(_key)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    return fernet.decrypt(data.encode()).decode()
