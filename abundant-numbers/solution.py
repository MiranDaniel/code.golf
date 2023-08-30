r=range
for q in r(201):
	a=1
	for i in r(2,int(q**0.5)+1):
		if q%i==0:
			a+=i;n=q//i
			if i!=n:a+=n
	if a>q>0:print(q)
