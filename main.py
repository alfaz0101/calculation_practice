import subprocess
from random import randint

while True:

    first_number = randint(1, 100)
    second_number = randint(1, 100)

    subprocess.run(["python3", "questions.py", f"{first_number}", f"{second_number}"])

    continue_answer = input("Want to Keep Going? ")

    if continue_answer.lower() == "yes":
        continue

    else:
        break