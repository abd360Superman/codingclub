import random
#To Import a module, you write 'import ModuleName'

#Random Number
#Both of the numbers are counted
#eg 1, 10 counts these numbers - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(random.randint(1, 10))

#Random Choice
#Takes an array, returns one random choice from the array

myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(myArr))

#Random Shuffle
#Takes an array, shuffles the same array

print(myArr)

random.shuffle(myArr)
print('After shuffling: ')
print(myArr)