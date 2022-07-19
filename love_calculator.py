sum1 = 0
sum2 = 0
name1 = (input("Enter you name: ")).lower()
name2 = (input("Enter your partners name: ")).lower()
check1 = "true"
check2 = "love"
for i in name1:
    for j in check1:
        if i == j:
            sum1 += 1
    for k in check2:
        if i == k:
            sum2 += 1

for i in name2:
    for j in check1:
        if i == j:
            sum1 += 1
    for k in check2:
        if i == k:
            sum2 += 1

love = f'{sum1}{sum2} %'
print(love)
