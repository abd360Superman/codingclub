
#For Loop (One Param Only)
for i in range(10):
    print(i)

#Two params
for i in range(9, 11):
    print(i)

#Three Params (Positive third)
for i in range(0, 100, 10):
    print('Are you %s years old' % str(i))

#Three Params (Negative third)
for i in range(100, 0, -10):
    print('Fine are you %s years old' % str(i))

#Loop through list
joke = ['Because', 7, 8, 9]
for i in joke:
    print(i)

