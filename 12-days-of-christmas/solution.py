g="A Partridge in a Pear Tree.|Two Turtle Doves|Three French Hens,|Four Calling Birds,|Five Gold Rings,|Six Geese-a-Laying,|Seven Swans-a-Swimming,|Eight Maids-a-Milking,|Nine Ladies Dancing,|Ten Lords-a-Leaping,|Eleven Pipers Piping,|Twelve Drummers Drumming,".split("|")
d="First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|Eleventh|Twelfth".split("|")
n="\n"
for i,y in enumerate(d,1):
	q=g[:i][::-1]
	g[1]+=", and"if i==1else""
	print(f"On the {y} day of Christmas\nMy true love sent to me{n}{n.join(q[:-1])+n if len(q)>1else ''}{q[-1]}",end=n*2)
