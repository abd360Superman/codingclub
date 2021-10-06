import time

x = time.time()
#Tells seconds passed from UTC 00:00, Jan 1, 1970

for i in range(1000):
    print(i)

print('The program took %s seconds to run' % (time.time() - x))