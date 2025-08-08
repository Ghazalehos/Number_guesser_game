import random

score = 100
random_number = random.randint(1, 100)

while True:
    input_number = input("Enter a number between 1 and 100:")
    if input_number == "q":
        print("bye!")
        break
    if not input_number.isdigit():
        print("please enter a valid number!")
        continue
    guess_number = int(input_number)
    if guess_number < random_number:
        print("Your guess is too low!")
        score -= 10
    elif guess_number > random_number:
        print("Your guess is too high")
        score -= 10
    else:
        score = max(score, 0)
        print(f"your guess is correct number! and your score is: {score}")
        break