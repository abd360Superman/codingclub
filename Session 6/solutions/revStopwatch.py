import time
secs = int(input('How many seconds should the timer run for? '))

for i in range(secs, 0, -1):
    print(i)
    time.sleep(1)
print('Done. ')