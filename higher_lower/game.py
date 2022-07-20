from gameData import data
from random import randint
from art import logo
print(logo)
end_of_game = False
score = 0
same_data = True

while not end_of_game:
    index1 = randint(0, len(data)-1)
    index2 = randint(0, len(data)-1)
    same_data = True
    while same_data:
        index2 = randint(0, len(data)-1)
        if index1 != index2:
            same_data = False
    name1 = data[index1]["name"]
    name2 = data[index2]["name"]
    follow_count1 = data[index1]['follower_count']
    follow_count2 = data[index2]['follower_count']

    print(f"Who is higher of {name1} V/s {name2}")
    guess = input("Enter your guess: ").lower()
    if ((guess == name1.lower()) and (follow_count1 > follow_count2)):
        print("Correct Guess")
        score += 1
        print(f"Score: {score}")
    elif ((guess == name2.lower()) and (follow_count1 < follow_count2)):
        print("Correct Guess")
        score += 1
        print(f"Score: {score}")
    elif ((int(guess) == 1) and (follow_count1 > follow_count2)):
        print("Correct Guess")
        score += 1
        print(f"Score: {score}")
    elif ((int(guess) == 2) and (follow_count1 < follow_count2)):
        print("Correct Guess")
        score += 1
        print(f"Score: {score}")

    else:
        print("You Lose")
        print(f"Score: {score}")
        end_of_game = True
