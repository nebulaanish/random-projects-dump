import os
from logo import logo
end_of_program = False
myValue = {
    "names": [],
    "bid_amount": []

}
print(logo)
key1 = "names"
key2 = "bid_amount"
maxindex = 0
n = int(input("Enter number of entries: "))

while end_of_program != True:
    for i in range(n+1):
        if end_of_program == True:
            break
        myValue[key1[i]] = input("Enter your name: ")
        myValue[key2[i]] = int(input("Enter your bid amount: "))
        user_feedback = input("Enter yes or no for more entries: ").lower()
        os.system('cls')
        if user_feedback == "no":
            end_of_program = True
maxindex = myValue[key2].index(max(myValue[key2]))
print(
    f"The winner is {myValue[key1[maxindex]]} with $ {myValue[key2[maxindex]]}")
