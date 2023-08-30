def s():
	d=["▲"]
	for i in range(4):sp=" "*(2**i);d=[sp+x+sp for x in d]+[x+" "+x for x in d]
	return d
print("\n".join(s()))
