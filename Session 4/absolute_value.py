print(abs(-10))
print(abs(10))

#Some code to get a negative absolute value!!
num = int(input('Enter number for Negative Absolute Value: '))
absval = 0

if num < 0:
    absval = num
else:
    absval = num - (num * 2)
print(absval)