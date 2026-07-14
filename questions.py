from random import randint
import threading
import time

#generates random numbers to multiply
first_number = randint(1, 100)
second_number = randint(1, 100)

#gets the answer and says if its correct or not
def generate_question():
    answer = int(input(f"{first_number} x {second_number} = "))
    if answer == first_number * second_number:
        print("Correct")
    else:
        print(f"Incorrect, the correct answer was {first_number * second_number}")

#creates a thread targetting towards the generate_question function
question_thread = threading.Thread(target=generate_question, daemon= True)

#gets the start time
start = time.perf_counter()

#starts the thread while also limiting its runtime (timeout)
question_thread.start()
question_thread.join(15.0)

#gets the end time
end = time.perf_counter()

#if timeout is reached print times up
if (end - start) // 1 == 15:
    print(f"Time's Up, the answer was {first_number * second_number}")