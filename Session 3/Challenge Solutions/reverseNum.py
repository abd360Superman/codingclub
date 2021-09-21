t = 87698
#Change this to change the result!
r = 0
while t != 0:
	r = r * 10
	r = r + t % 10
	t = int(t / 10)

print(r)