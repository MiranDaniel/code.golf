b=lambda x,y=0:f"{x if x!=0else'no more'} bottle{'s'if x>1or x==0else''} of beer{' on the wall'if y==0else''}"
for i in range(99,0,-1):print(f"{b(i)}, {b(i,1)}.\nTake one down and pass it around, {b(i-1)}.\n")
print(f"{b(0).capitalize()}, {b(0,1)}.\nGo to the store and buy some more, {b(99)}.")
