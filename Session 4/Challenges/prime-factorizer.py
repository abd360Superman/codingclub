ay = 2
bee = 78
#The bee variable is basically the number you will prime factorize. Change it and see that the results will change, too!

while bee != 0:
    y = bee / ay
    x = int(y)

    if y == x and y != 1:
        print('%s x' % ay)
        bee = y
    elif y == 1:
        print('%s' % bee)
        break
    else:
        ay = ay + 1
