import sys
for s in sys.argv[1:]:
	c,j=0,10
	for i in s.replace("-",""):c-=j*int(i);j-=1
	print(s+f"{'X'if c%11>9else c%11}")
