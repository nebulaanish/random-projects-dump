from random import randint
from art import logo
print(logo)
difficulty_input = input("Enter easy or hard level: ").lower()
difficulty_level = {
    "easy": 10,
    "hard": 5,
}
difficulty_input = int(difficulty_level[difficulty_input])


def gameLogic(limit):
    end_of_program = False
    guessCount = 0
    flag = randint(1, 100)
    while not end_of_program:
        guessCount += 1
        inputNumber = int(
            input(f"You have {int(limit)+1 -guessCount} turns: "))
        if inputNumber == flag:
            end_of_program = True
            print("Yayyy!! You guessed it right")

        elif inputNumber < flag:
            print("Guess is low")
        elif inputNumber > flag:
            print("Guess is high")
        if guessCount >= int(limit):
            end_of_program = True
            print(f"You exhausted your chances of guessing {flag}")


gameLogic(difficulty_input)
