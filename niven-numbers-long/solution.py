i=0
while i<10001:
	i+=1
	if i%sum(map(int,str(i)))<1:print(i)