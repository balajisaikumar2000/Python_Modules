from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

message = "This is password"

encrypted = f.encrypt(message.encode())
print(encrypted)
decrypted = f.decrypt(encrypted)
print(decrypted)
