year = int(input("Enter a year to test: "))
if year % 400 == 0:
    print("Leap Year")
else:
    if (year % 4 == 0) and ((year % 100) != 0):
        print("Leap year")
    else:
        print("Not a leap Year")
