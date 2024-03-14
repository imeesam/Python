import random
import string

def pas_genrtor():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    character = lowercase_letters + uppercase_letters + digits
    passw = "".join(random.choice(character) for i in range(8))
    return passw

print(pas_genrtor())
