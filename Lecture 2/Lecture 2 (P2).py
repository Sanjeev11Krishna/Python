#Formatted Strings
num = 3000
frac = 1/3
print(num * frac, 'is', frac * 100, '% of' num) # output: 1000.0 is 33.3333333333333 % of 3000
print(num * frac, 'is', str(frac * 100) + '% of', num) # output: 1000.0 is 33.3333333333333% of 3000

#expression in curly braces evaluated at runtime, gets converted to strings, and concatenate to the strings preceding them
print(f'{num *frac} is {frac * 100}% of {num}') #output: 1000.0 is 33.3333333333333% of 3000

#Relational operators
print('a' == 'A') #output: False
print(2 < 3) #output: True
print(not(2 < 3)) # output: False
print((2 < 3) and(3 < 4)) #output: True
print((2 < 3) and (3 > 4)) # output: False

pset_time = 15
sleep_time = 8
print(sleep_time < pset_time) #output: False

drive = True
drink = False
print(drink and drive) #output: False

#Guessing game
secret = 5
guess = int(input("Guess a number : ")) #input: 4
print(guess == secret) #output: False
