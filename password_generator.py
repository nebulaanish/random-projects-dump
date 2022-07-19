import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

total_number = int(input("Enter number of characters: "))
string_number = int(input("Enter number of strings: "))
symbol_number = int(input("Enter number of symbols: "))
num_number = int(input("Enter number of numbers: "))

password = []
final = ""
if (string_number+symbol_number+num_number) == total_number:
    for i in range(0, string_number+1):
        password.append(random.choice(letters))
    for i in range(0, symbol_number+1):
        password.append(random.choice(symbols))
    for i in range(0, num_number+1):
        password.append(random.choice(numbers))
    for i in range(0, total_number+1):
        final += password[i]
    print(f'{final}')
else:
    print("The number ratio is wrong")
