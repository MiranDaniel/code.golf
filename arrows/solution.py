import sys
t,d=[0,]*2,{}
for i in"↙←↖↓↑↘→↗|↲⇐↰⇓⇑↳⇒↱|⇙⇦⇖⇩⇧⇘⇨⇗".split("|"):d=dict(zip(i,[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]),**d)
for a in sys.argv[1:]:t=[x+y for x,y in zip(t,d.get(a,(0,0)))];print(*t)