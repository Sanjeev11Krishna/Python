#break
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
    mysum += 1
print(mysum)

#try it - no of even nos
n = 0
for i in range(5):
    if i%2 == 0:
        n += 1
print(n) #3
n = 0
for i in range(10):
    if i%2 == 0:
        n += 1
print(n) #5
n = 0
for i in range(2, 9, 3):
    if i%2 == 0:
        n += 1
print(n) #2
n = 0
for i in range(-4, 6, 2):
    if i%2 == 0:
        n += 1
print(n) #5
n = 0
for i in range(5, 6):
    if i%2 == 0:
        n += 1
print(n) #0

#Strings and Loops
s="Demo loops - fruit loops"
for i in range(len(s)):
    if s[i]=='i' or s[i]=='u':
        print("There is an i or u")

#iterates through a string
for char in s:
    if char=='i' or char=='u':
        print("There is an i or u")

for char in s:
    if char in 'iu':
        print("There is an i or u")

#Robot cheerleaders
an_letters="aefhilmnorsxAEFHIMNORSX"

word=input("I will cheer for you! Enter a word: ")
times=int(input("Enthusiasm level (1-10): "))

for c in word:
          if c in an_letters:
              print(f'Give me an {c}: {c}')
          else:
              print(f'Give me a {c}: {c}')
print("What's that spell?")
for i in range(times):
    print(word,'!!!')

#Try it
s="abca"
seen=''
count=0
for char in s:
    if char not in seen:
        seen = seen+char
        count+=1
    else:
        pass 
print(count)
print(len(seen))

#Guess-and-Check algorithm
#For positive input
guess = 0
x = int(input("Enter an integer: "))
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print("Square root of", x, "is", guess)
    print("So", x, "is a perfect square")
else:
    print(x, "is not a perfect square")

#For negative input
guess = 0
neg_flag=False
x = int(input("Enter an integer: "))
if x<0:
    neg_flag=True
while guess**2 < x:
    guess = guess + 1

if guess**2 == x:
    print("Square root of", x, "is", guess)
    print("So", x, "is a perfect squaree")
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


#Try it
secret=int(input("Enter the number: "))
for i in range(1,11):
    if i==secret:
        print("The number is found")
   
#else print not found using boolean flag
found=False
secret=int(input("Enter the number: "))
for i in range(1,11):
    if i==secret:
        print("The number is found")
        found=True
if not found:
    print("The number  is not found")
        

#Guess and Check cube root
#Positive cubes
cube=int(input("Enter an integer: "))
for guess in range(cube+1):
    if guess**3==cube:
        print("The cube root of ", cube, "is", guess)

#Negative cubes
cube=int(input("Enter an integer: "))
for guess in range(abs(cube)+1):  
    if guess**3==cube:
        if cube<0:
            guess=-guess      
        print("The cube root of ", cube, "is", guess)

#Just a little faster
cube = int(input("Enter an integer: "))
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))

#Word problem
for alyssa in range(11):  
    for ben in range(11):  
        for cindy in range(11):  
            total = (alyssa + ben + cindy == 10)  
            two_less = (ben == alyssa - 2)  
            twice = (cindy == 2 * alyssa)  
            if total and two_less and twice:  
                print(f"Alyssa sold {alyssa} tickets")  
                print(f"Ben sold {ben} tickets")  
                print(f"Cindy sold {cindy} tickets")

#For largest numbers
for alyssa in range(1001):  
    ben = max(alyssa - 20, 0) 
    cindy = alyssa * 2  
    if ben + cindy + alyssa == 1000:  
        print("Alyssa sold " + str(alyssa) + " tickets")  
        print("Ben sold " + str(ben) + " tickets")  
        print("Cindy sold " + str(cindy) + " tickets")

#Binary Numbers
x = 0
for i in range(10):
    x += 0.1
print(x == 1)
print(x, "==", 10 * 0.1)

#Decimal to binary conversions
num=int(input("Enter an integer: "))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
print(result)

#For negative numbers
num=int(input("Enter an integer: "))
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if is_neg:
    result = '-' + result
print(result)
