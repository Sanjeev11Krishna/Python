#branching
pset_time = 22
sleep_time = 1
if(pset_time + sleep_time) > 24:
    print("impossible")
elif(pset_time + sleep_time) == 24:
    print("full schedule")
else:
    leftover = abs(24 - (pset_time + sleep_time))
    print(leftover, 'h of free time')
print('end of the day')

if x == y:
    print(x, ' is the same as ', y)
    print('they are equal')
else:
    print(x, ' is different from ', y)

#nested branching
x = float(input("Enter a number for x : "))
y = float(input("Enter a number for y : "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("Therefore, x/y is", x / y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")

#guessing game
secret = 5
guess = int(input("Guess a number : "))
if guess > secret:
    print("too high")
elif guess == secret:
    print("Equal")
else:
    print("too low")
    
