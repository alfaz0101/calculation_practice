from random import randint
import time
import threading

first_number = randint(1, 100)
second_number = randint(1, 100)

def generate_question():
    answer = int(input(f"{first_number} x {second_number} = "))
    if answer == first_number * second_number:
        print("Correct")
    else:
        print(f"Incorrect, the correct answer was {first_number * second_number}")
generate_question()