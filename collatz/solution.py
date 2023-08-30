for n in range(1,1001):
	t=0
	while 1!=n:t+=1;n=n/2if n%2==0else n*3+1
	print(t)
