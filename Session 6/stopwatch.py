import time

secs = int(input('How many seconds should the stopwatch last for? '))

for i in range(secs):
    print(i+1)
    #time.sleep(seconds)
    #Temporarily stops the thread for given seconds
    time.sleep(1)