import hashlib

def encrypt_password(password: str):
    salt = b'\xf8\x16\x08\x94\x19\x8c\x15\x9a\x1a\x8f\x14\x9f' # a random byte string of your choice
    iterations = 100000 # the number of iterations
    key = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, iterations)
    return salt + key

def check_password(password: str, encrypted_password: bytes) -> bool:
    salt = encrypted_password[:12]
    key = encrypted_password[12:]
    iterations = 100000
    new_key = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, iterations)
    return key == new_key

password = input("Enter the password: ")

encrypted_password = encrypt_password(password)
print(f'Encrypted password: {encrypted_password}')

password_check = input("Enter the password again: ")
is_password_valid = check_password(password_check, encrypted_password)
print(f'Is password valid: {is_password_valid}')

