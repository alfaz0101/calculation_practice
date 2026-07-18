import subprocess
from random import randint
from score_handling import delete_score, get_score, get_score_length

delete_score()

while True:

    first_number = randint(1, 100)
    second_number = randint(1, 100)

    subprocess.run(["python3", "questions.py", f"{first_number}", f"{second_number}"])

    continue_answer = input("Want to Keep Going? ")

    if continue_answer.lower() == "yes":
        continue

    else:
        break

score_percentage = get_score() * 100 / get_score_length()

print(f"You answered {get_score()}/{get_score_length()} correct, or roughly {score_percentage}% correct")