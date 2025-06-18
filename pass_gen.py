import random

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password with specified criteria."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_uppercase else ''
    numbers = '0123456789' if use_numbers else ''
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/' if use_special_chars else ''

    all_characters = lowercase + uppercase + numbers + special_chars

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    password = []
    
    # Ensure at least one character from each selected category
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random choices from all characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the resulting password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    password = generate_password(length=n, use_uppercase=upper, use_numbers=numbers, use_special_chars=special)
    print("Generated Password:", password)


if __name__ == "__main__":
    n = int(input("Enter the desired password length (minimum 4): "))
    upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    if n < 4:
        print("Password length must be at least 4 characters.")
    else:
        main()
# This code generates a random password based on specified criteria.
# It ensures that the password contains at least one uppercase letter, one number, and one special character if those options are selected.