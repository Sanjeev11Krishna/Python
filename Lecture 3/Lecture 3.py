#function for setting background  name
def set_background(background_name):
    print(f"background set to: {background_name}")

exit_right = True
if exit_right:
    set_background('woods_background')
    if  exit_right:
        set_background('woods_background')
        if exit_right:
            set_background('woods_background')
        else:
            set_background('exit_background')
    else:
        set_background('exit_background')
else:
    set_background('set_background')

while exit_right:
    set_background('woods_background')
    user_ip = input('Which way to go?(left/right): ').lower()
    if  user_ip == 'right':
        set_background('exit_background')
        exit_right = False
    else:
        print('You chose left. Try Again')

#Lost Forest using while loop
where = input("You're in the Lost Forest. Go left or right? : ")
while where == 'right':
    where = ipnut('Go left or right? ')
print('You got Out!')

#for numbers
n = int(input('Enter a number ( >0):'))
while n > 0:
    print('x')
    n = n - 1

#Sad face
n = 0
where = input('Go left or right? ')
while where == 'right':
    n += 1
    print(n)
    if n > 2:
        print(":(")
    where = input('Go left or right? ')
print('You got out!')

#iterating numbers using while
n = 0
while n < 5:
    print(n)
    n += 1
    
#factorial using while
x = 5
i = 1
fac = 1
while i <= x:
    fac *=i
    i += 1
printf(f"{x} factorial is {fac}")

#iterating numbers using for
for i in range(5):
    print(i)
for i in range(1, 4, 2):
    print(i * 2)
for i in range(4,0,-1):
    print('$'*i)

#running sum
mysum = 0
for i in range(10):
    mysum += i
print(mysum)

#factorial using  for
x = 5
fac = 1
for i in range(1, x+1):
    fac *= i
print(f"{x} factorial is {fac}")
