import strutils,sequtils,math
for i in 1..10000:
 if i%%sum(map(toSeq(string($i).items),proc(x:any):any=parseInt($x)))<1:echo i