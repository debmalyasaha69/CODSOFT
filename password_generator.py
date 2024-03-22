import random
import string


def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_specialchars=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specialchars:
        special_characters = "!@#$%^&*()_+=-{}[]|\/:;<>,.?~"
        characters += ''.join(random.choice(special_characters))
    if not characters:
        raise ValueError(
            "At least one character set (uppercase, lowercase, digits, special characters) must be enabled.")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        # Prompt the user for complexity options
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Password length must be a positive integer.")
            return

        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)

        # Display the generated password
        print("Generated Password:", password)

    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
