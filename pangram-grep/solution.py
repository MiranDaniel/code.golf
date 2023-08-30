import sys
for a in sys.argv[1:]:
	s="".join([chr(i)for i in range(97,123)])
	for i in a.lower():s=s.replace(i,"")
	if len(s)==0:print(a)
