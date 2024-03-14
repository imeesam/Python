import random
import string

gue = random.choice(string.ascii_lowercase)
print("Welcome to letter guessing game.")
n=7
while n>=1:
    n-=1
    usr= input("Guess any letter:")
    if usr == gue:
        print("Congratulations! you guessed correct letter.")
        break
    else:
        print(f"{n} turns left")
if n==0:
    print(f"You lost. The correct letter was {gue}")
