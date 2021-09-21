#Simple Func - No Input/Output
def hw_5():
    for i in range(5):
        print('Hello World!')
hw_5()
#Func - No Output, yes Input
def print_itrtxt(iter, txt):
    for i in range(iter):
        print(txt)
print_itrtxt(9, 'Howdy!')

#Advanced Func - Yes Input/Output
def myop(num):
    newnum = num * (num + num ** 2) + (num * num)
    return newnum
print(myop(27))
