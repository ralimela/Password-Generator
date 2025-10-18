import secrets
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    alphabet = letters + digits + punctuation
    
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c in letters for c in password) and
                any(c in digits for c in password) and
                any(c in punctuation for c in password)):
            return password

if __name__ == "__main__":
    try:
        pwd_len = int(input("Enter the desired password length: "))
        pwd = generate_password(pwd_len)
        print(f"Your generated password is: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
