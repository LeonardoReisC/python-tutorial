# recommended for sensitive data
import secrets
import string as s

random = secrets.SystemRandom()  # good practice

# password generator
print("".join(random.choices(s.ascii_letters + s.digits + s.punctuation, k=8)))