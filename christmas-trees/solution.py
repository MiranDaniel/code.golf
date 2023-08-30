p=print
def t(s,c,o=1):
	p(" "*s+"*"*o,end="")
	if s!=1:p();t(s-1,c,o+2)
	else:p("\n"+" "*c+"*")
for i in range(3,10):
	if i not in(3,10):p()
	t(i,i)
