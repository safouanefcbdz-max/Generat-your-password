import secrets
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Error: You must select at least one character type!"
    
    return ''.join(secrets.choice(characters) for _ in range(length))

# Main program
print("Password Generator")
print("-" * 40)

try:
    # Ask for length
    length = int(input("Enter password length (min 8): "))
    
    if length < 8:
        print("Warning: Minimum 8 characters recommended")
        length = max(8, length)
    
    print("\nCharacter options:")
    
    # Ask for character types
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
    use_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols (!@#$...)? (y/n): ").lower() == 'y'
    
    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    print("\n" + "=" * 40)
    print("Your password:", password)
    print("Length:", length, "characters")
    print("=" * 40)
    
except ValueError:
    print("Error: Please enter a valid number")