from logo import logo
from actions import add, sub, product, divide
import os


def calculator():
    print(logo)
    print('Calculator App')
    num1 = float(input("First number: "))
    action_dictionary = {
        "+": add,
        "-": sub,
        "*": product,
        "/": divide,
    }
    program_continue = True
    for i in action_dictionary:
        print(f"{i}")
    while program_continue == True:
        print("Enter an operation")
        action = input()
        num2 = float(input("Next Number: "))
        answer = action_dictionary[action](num1, num2)
        os.system("cls")
        print(logo)
        print(f"{num1} {action} {num2} = {answer}")
        user_feedback = input(
            f"Enter y to continue with {answer} n to do new calculation or 'exit' to exit ").lower()
        if user_feedback == "y":
            num1 = answer
        elif user_feedback == "exit":
            break
        else:
            calculator()


calculator()
