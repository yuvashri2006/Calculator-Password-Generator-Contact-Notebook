import random
import string
length = int(input("Enter the desired length of the password: "))
def generate_password(length):
    letters_numbers = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_numbers) for _ in range(length))
password = generate_password(length)
print("Generated Password:", password)
