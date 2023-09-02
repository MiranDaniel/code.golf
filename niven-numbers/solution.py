i=0
while i<101:
	i+=1
	if i%sum(map(int,str(i)))<1:print(i)