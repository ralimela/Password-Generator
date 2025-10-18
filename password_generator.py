import secrets
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    punctuation = string.punctuation if use_symbols else ''
    alphabet = letters + digits + punctuation

    if not alphabet:
        raise ValueError("No character sets selected for password generation.")

    # Ensure password contains at least one character from each selected category
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c in letters for c in password) and
            (not use_digits or any(c in digits for c in password)) and
            (not use_symbols or any(c in punctuation for c in password))):
            return password

if __name__ == "__main__":
    try:
        pwd_len = int(input("Enter the desired password length: "))
        use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
        pwd = generate_password(pwd_len, use_digits, use_symbols)
        print(f"Your generated password is: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
