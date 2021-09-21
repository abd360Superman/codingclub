x = 24
#Change this to change the result!

counter = int(x / 2)
print(counter)

factors = []
for i in range(1, counter+1):
    if x % i == 0:
        factors.append(i)

factors.append(x)

print(factors)
