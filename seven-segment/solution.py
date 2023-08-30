import sys
d=[[],[],[]];m=int
for i in sys.argv[1:][0]:
	for j in range(3):d[j]+="".join([" _|"[m(i)-1] for i in str(m("73B182B#69F7399#73831F9#7383133#6A2A7E9#73B36A3#73B376B#7380A19#73B3F3B#73B3E73".split("#")[m(i)],16))])[j*3:j*3+3]
for i in d:print("".join(i))
