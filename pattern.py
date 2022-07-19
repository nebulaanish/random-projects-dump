num = int(input("enter a number"))

def spacefunc(num):
    space = 0
    space = num - i -1
    return int(space/2)

for i in range(1,num-1,2):
    print(spacefunc(num)*" " + i * "*" + spacefunc(num)*" ")

for i in range(num-1,0,-2):
    print(spacefunc(num)*" " + i * "*" + spacefunc(num)*" ")




   