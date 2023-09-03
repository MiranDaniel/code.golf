import sys
n,m,h,l,e,p=*[0]*4,enumerate,sys.argv[1].splitlines()
for x,i in e(p):
	for y,j in e(i):
		if"S"==j:n,m=x,y
		if"E"==j:h,l=x,y
q,b,f,c=[(n,m)],{},[],(h,l)
while q:
	x,y=q.pop(0)
	if(x,y)==(h,l):break
	for t,r in[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
		if 0<x<len(p)and 0<y<len(p[0])and"#"!=p[t][r]and(t,r)not in b:b[(t,r)]=(x,y);q.append((t,r))
while c!=(n,m):f.append(c);c=b[c]
o=[list(r)for r in p];f.reverse()
for x,y in f:
	if o[x][y]not in"SE":o[x][y]="."
for r in o:print(''.join(r))