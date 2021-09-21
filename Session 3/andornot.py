x = 8
y = 7

#This line will only execute if both statements are true
if x == 8 and y == 7:
    print('Hey!')
if x != 8 and y == 7:
    print('Who are you?')
if x != 8 and y != 7:
    print('How do you do?')

#This line will execute if any or all of the conditions are true
if x == 8 or y == 7:
    print('Hey!')
if x != 8 or y == 7:
    print('Who are you?')
if x != 8 or y != 7:
    print('How do you do?')

# NOT only executes line if the condition is false
if not x == 8:
    print('X is not 8!')
else:
    print('X is 8!')
